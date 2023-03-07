#!/usr/bin/env python3

"""

This script builds zip files to be released to GitHub.

The zip files are only updated if the files are changed or renamed.

"""
import hashlib
import json
import re
import sys
import textwrap
import zipfile

from difflib import Differ
from pathlib import Path


def name_clean(name):
    return re.sub(r'[^a-zA-Z]+', '', name.replace('.zip', '')).lower()

def name_match(name, all_names):
    name_cleaned = name_clean(name)
    for a_name in all_names:
        if name_cleaned == name_clean(a_name):
            return a_name

    return None


def build_files(root, dest_path, max_depth=None, *, want_dirs=False):
    stack = [root]
    while len(stack) > 0:
        path = stack.pop(0)

        for source_name in path.iterdir():
            if source_name.name.startswith('.'):
                continue

            temp = source_name.relative_to(root)
            if max_depth is not None and len(temp.parts) > max_depth:
                continue

            if source_name.is_dir():
                stack.append(source_name)
                if not want_dirs:
                    continue

            dest_name = dest_path / temp
            yield source_name, dest_name


def build_zip(base_zip_name, root_path, paths, config, dry_run=False):
    """
    TODO: document it
    """

    ## Each zip has a zip file, a .sha256 file, and a .sha256sum file.
    zip_name = config['RELEASE_DIR'] / base_zip_name
    check_name = config['CHECK_DIR'] / (base_zip_name.rsplit('.', 1)[0] + '.sha256')
    shasum_name = config['RELEASE_DIR'] / (base_zip_name + '.sha256sum')

    # Build up a list of all files needed for the zip, and their location on the file system
    all_files = []
    for path in paths:
        max_depth = None
        if isinstance(path, (list, tuple)):
            if len(path) == 2:
                real_name, internal_name = path
            elif len(path) == 3:
                real_name, internal_name, max_depth = path
            else:
                print(f"  - Bad path in paths, length of tuple must be 2 or 3: {path}, failing to build zip.")
                return
        else:
            real_name = internal_name = path

        full_name = Path(root_path) / real_name
        if full_name.is_file():
            all_files.append((str(internal_name), str(full_name)))
        elif full_name.is_dir():
            for src, dest in build_files(full_name, internal_name, max_depth):
                all_files.append((str(dest), str(src)))
        else:
            print(f"  - {str(full_name)!r} failing to build zip.")
            return


    # IF we get this far, we should create the RELEASE_DIR / CHECK_DIR
    if not config['RELEASE_DIR'].is_dir():
        config['RELEASE_DIR'].mkdir()
    if not config['CHECK_DIR'].is_dir():
        config['CHECK_DIR'].mkdir()

    # Sort the files so we always get the same result.
    all_files.sort(key=lambda x: x[0])

    # Make a hash of each zip file + hash
    main_hash = hashlib.sha256()
    all_digests = []
    for file_pair in all_files:
        # Hash file
        file_hash = hashlib.sha256()
        with open(file_pair[1], 'rb') as fh:
            file_hash.update(fh.read())

        file_digest = f'{file_pair[0]}:{file_hash.hexdigest()}'
        all_digests.append(file_digest)

        # Add to main hash
        main_hash.update(f"{file_digest}\n".encode('utf-8'))

    # Keep our newly created hashes
    new_digest = main_hash.hexdigest()
    all_digests.append(f'{str(zip_name)}:{new_digest}')

    if zip_name.exists():
        if check_name.is_file():
            with open(check_name, 'r') as fh:
                ## Get the last line, read the sha256 from it.
                old_digests = fh.read().strip().split('\n')
                old_digest = old_digests[-1].rsplit(':', 1)[-1]

            # See if the files have changed.
            if new_digest == old_digest:
                print('  - File is up to date.')
                return
            else:
                # Build up what files have changed
                changes = {}
                differ = Differ()
                for line in differ.compare(old_digests[:-1], all_digests[:-1]):
                    # line = "  <FILENAME>:<SHA256SUM>"
                    mode = line[:2]
                    name = line[2:].split(":", 1)[0]
                    if mode == '- ':
                        # File is removed.
                        changes[name] = 'Removed'
                    elif mode == '+ ':
                        if name in changes:
                            # If the file was already seen, its been removed, and readded, which means modified.
                            changes[name] = 'Modified'
                        else:
                            # File is just added.
                            changes[name] = 'Added'

                print("  - Files changed")
                for name, mode in changes.items():
                    print(f"    - {mode} {name}")

    if dry_run:
        return

    print('  - Building Zip')
    with zipfile.ZipFile(zip_name, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for file_pair in all_files:
            zf.write(file_pair[1], file_pair[0])

    print('  - Recording sha256sum')
    final_hash = hashlib.sha256()
    with open(zip_name, 'rb') as fh:
        final_hash.update(fh.read())

    final_digest = final_hash.hexdigest()

    with open(shasum_name, 'w') as fh:
        fh.write(f'{final_digest} *{Path(zip_name).name}')

    print('  - Recording Checkfile')
    with open(check_name, 'w') as fh:
        fh.write('\n'.join(all_digests))


def do_build(config, build_configs, args):
    """
    Builds a zip file based on build_zip.json, usage:

    {command} build all
    {command} build <zip name>
    """

    if len(args) == 0:
        args.append('all')

    if args[0] == 'all':
        print("Building all zips:")

        for zip_name, zip_config in build_configs.items():
            print(f"- {zip_name}")
            if zip_config['disabled'].is_file():
                print("  - disabled skipping")
                continue

            build_zip(
                zip_config['zip_file'],
                zip_config['directory'],
                zip_config['files'],
                config)
    else:
        print("Building selected zips:")

        for name in args:
            match_name = name_match(name, build_configs.keys())
            if match_name is None:
                print(f"- Unknown zip {name!r}")
                continue

            print(f"- Building {build_configs[match_name]['zip_file']}")
            
            build_zip(
                build_configs[match_name]['zip_file'],
                build_configs[match_name]['directory'],
                build_configs[match_name]['files'],
                config)


def do_check(config, build_configs, args):
    """
    Checks a the files changed based on build_zip.json, checks zips even if they are disabled, usage:

    {command} check all
    {command} check <zip name>
    """

    if len(args) == 0:
        args.append('all')

    if args[0] == 'all':
        print("Checking all zips:")

        for zip_name, zip_config in build_configs.items():
            print(f"- {zip_name}")

            build_zip(
                zip_config['zip_file'],
                zip_config['directory'],
                zip_config['files'],
                config, dry_run=True)
    else:
        print("Checking selected zips:")

        for name in args:
            match_name = name_match(name, build_configs.keys())
            if match_name is None:
                print(f"- Unknown zip {name!r}")
                continue

            print(f"- {build_configs[match_name]['zip_file']}")
            
            build_zip(
                build_configs[match_name]['zip_file'],
                build_configs[match_name]['directory'],
                build_configs[match_name]['files'],
                config, dry_run=True)


def do_enable(config, build_configs, args):
    """
    Enables a port being build by "build all"

    {command} enable all
    {command} enable <zip name>
    """
    if len(args) == 0:
        print("No <zip name> specified, see help for usage")
        do_help(config, build_configs, ['enable'])
        return

    enable_count = 0
    if args[0] == 'all':
        print("Enabling all zips:")

        for zip_name, zip_config in build_configs.items():
            if zip_config['disabled'].is_file():
                zip_config['disabled'].unlink()
                print(f"- {zip_config['zip_file']} enabled")
                enable_count += 1

        print(f"- Enabled {enable_count} / {len(build_configs)} items")

    else:
        print("Enabling selected zips:")

        for name in args:
            match_name = name_match(name, build_configs.keys())
            if match_name is None:
                print(f"- Unknown zip {name!r}, skipping")
                continue

            if build_configs[match_name]['disabled'].is_file():
                build_configs[match_name]['disabled'].unlink()
                print(f"- {build_configs[match_name]['zip_file']} enabled")
                enable_count += 1

        print(f"- Enabled {enable_count} / {len(args)} items")


def do_disable(config, build_configs, args):
    """
    Disable a port being build by "build all", it will still be built by "{command} build <zip name>"

    The zip is disabled by making a file named ".build_disable" in the directory with "build_zip.json"

    {command} disable all
    {command} disable <zip name>[ <zip name>]+
    """

    disable_count = 0
    if args[0] == 'all':
        print("Disabling all zips:")

        for zip_name, zip_config in build_configs.items():
            if not zip_config['disabled'].is_file():
                zip_config['disabled'].touch()
                print(f"- {zip_config['zip_file']} disabled")
                disable_count += 1

        print(f"- Disabled {disable_count} / {len(build_configs)} items")

    else:
        print("Disabling selected zips:")

        for name in args:
            match_name = name_match(name, build_configs.keys())
            if match_name is None:
                print(f"- Unknown zip {name!r}, skipping")
                continue

            if not build_configs[match_name]['disabled'].is_file():
                build_configs[match_name]['disabled'].touch()
                print(f"- {build_configs[match_name]['zip_file']} disabled")
                disable_count += 1

        print(f"- Enabled {disable_count} / {len(args)} items")


def do_list(config, build_configs, args):
    """
    Lists all ports, and whether they're enabled or not.

    {command} list
    """

    max_name = max(map(lambda x: len(x['zip_file']), build_configs.values()))

    print("Available zips:")
    for zip_name, zip_config in build_configs.items():
        print(f"- {zip_config['zip_file']:{max_name}s} - {zip_config['disabled'].is_file() and 'Disabled' or 'Enabled'}")


def do_new(config, build_configs, args):
    """
    Makes a new zip build using the template folder. This will replace all
    instances of "template" and "Template" to whatever the new name of the zip is.

    {command} new "BobbleJump"
    """

    if len(args) == 0:
        print("No <zip name> specified, see help for usage")
        do_help(config, build_configs, ['new'])
        return

    name = args[0]

    def name_swap(input_text):
        return input_text.replace('Template', name).replace('template', name.lower())

    match_name = name_match(name, build_configs.keys())
    if match_name is not None:
        print(f"Error: {name} is the same as {match_name}, zip build already exists.")
        return

    if name == name.lower():
        print(f"Warning: having {name} in all lower case is not recommended.")

    print(f"Making new zip build {name}")
    for src_file, dst_file in build_files(
            config['SCAN_DIR'] / 'template', config['SCAN_DIR'] / name, want_dirs=True):
        dst_file = Path(name_swap(str(dst_file)))

        print(f"- Creating {dst_file}")

        if src_file.is_dir():
            dst_file.mkdir(mode=0o755, parents=True)
            continue

        dst_parent = dst_file.parent
        if not dst_parent.is_dir():
            dst_parent.mkdir(mode=0o755, parents=True)

        with open(src_file, 'r') as fh:
            src_data = fh.read()

        dst_data = name_swap(src_data)

        if dst_file.suffix == '.sh':
            mode = 0o755
        else:
            mode = 0o666

        with open(dst_file, 'w', mode) as fh:
            fh.write(dst_data)


def do_help(config, build_configs, args):
    """
    Shows general help or help for a particular command.

    {command} help
    {command} help list
    """
    command = sys.argv[0]

    if len(args) > 0:
        if args[0].lower() not in all_commands:
            print(f"Error: unknown help command {args[0]!r}")
            do_help(config, build_configs, [])
            return

        print(textwrap.dedent(all_commands[args[0].lower()].__doc__.format(command=command)).strip())
        return

    print(f"{command} <build|enable|disable|list> <all|PORT1> [.. PORT2]")
    print(f"{command} <help> <command>")
    print()
    print("All available commands: " + (', '.join(all_commands.keys())))


all_commands = {
    'build':    do_build,
    'help':     do_help,
    'enable':   do_enable,
    'disable':  do_disable,
    'check':    do_check,
    'list':     do_list,
    'new':      do_new,
    }


def main(args):
    # TODO: make this a config file ?
    config = {
        'SCAN_DIR': Path('.'),
        'RELEASE_DIR': Path('releases'),
        'CHECK_DIR': Path('.releases'),
        }

    # Find all zips
    all_configs = {}

    for json_file in sorted(config['SCAN_DIR'].glob('*/build_zip.json'), key=lambda x: str(x).lower()):
        try:
            with open(json_file, 'r') as fh:
                build_config = json.load(fh)

            if name_clean(build_config['zip_file']) == 'template':
                continue

            config_name = build_config['zip_file'].rsplit('.', 1)[0]
            if not 'files' in build_config:
                raise KeyError('files')

            build_config['disabled'] = (json_file.parent / '.build_disable')
            build_config['directory'] = json_file.parent
            all_configs[config_name] = build_config

        except json.decoder.JSONDecodeError as err:
            print(f"- Error parsing {json_file!r}: {err!r}")
            continue
        except KeyError as err:
            print(f"- Missing key {err!r} in {json_file}")
            continue

    if len(args) == 1:
        print('No commands given, assuming "build all", try "help" for commands available.')

        all_commands['build'](config, all_configs, ['all'])
        return

    if args[1].lower() not in all_commands:
        print(f'Command {args[1]!r} not found.')
        all_commands['help'](config, all_configs, [])
        return

    all_commands[args[1].lower()](config, all_configs, args[2:])


if __name__ == '__main__':
    main(sys.argv)
