#!/usr/bin/env python3

"""

This script builds zip files to be released to GitHub.

The zip files are only updated if the files are changed or renamed.

"""
import hashlib
import json
import zipfile
from pathlib import Path
from difflib import Differ


VERBOSE=False

def build_files(root, dest_path, max_depth=None):
    stack = [root]
    while len(stack) > 0:
        path = stack.pop(0)

        for source_name in path.iterdir():
            if source_name.name.startswith('.'):
                continue

            if source_name.is_dir():
                stack.append(source_name)
                continue

            temp = source_name.relative_to(root)
            if max_depth is not None and len(temp.parts) > max_depth:
                continue

            dest_name = dest_path / temp
            yield source_name, dest_name


def build_zip(base_zip_name, root_path, paths, config):
    """
    TODO: document it
    """

    ## Each zip has a zip file, a .sha256 file, and a .sha256sum file.
    zip_name = config['RELEASE_DIR'] / base_zip_name
    check_name = config['CHECK_DIR'] / (base_zip_name.rsplit('.', 1)[0] + '.sha256')
    shasum_name = config['RELEASE_DIR'] / (base_zip_name + '.sha256sum')

    print(f'Checking {str(zip_name)}')

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
                print(f"- Bad path in paths, length of tuple must be 2 or 3: {path}, failing to build zip.")
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
            print(f"- {str(full_name)!r} failing to build zip.")
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
                print('- File is up to date.')
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

                print("- Files changed")
                for name, mode in changes.items():
                    print(f"  - {mode} {name}")

    print('- Building Zip')
    with zipfile.ZipFile(zip_name, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for file_pair in all_files:
            zf.write(file_pair[1], file_pair[0])

    print('- Recording sha256sum')
    final_hash = hashlib.sha256()
    with open(zip_name, 'rb') as fh:
        final_hash.update(fh.read())

    final_digest = final_hash.hexdigest()

    with open(shasum_name, 'w') as fh:
        fh.write(f'{final_digest} *{Path(zip_name).name}')

    print('- Recording Checkfile')
    with open(check_name, 'w') as fh:
        fh.write(''.join(all_digests))


config = {
    'RELEASE_DIR': Path('releases'),
    'CHECK_DIR': Path('.releases'),
    }

# 
for json_file in Path('.').glob('*/build_zip.json'):
    try:
        with open(json_file, 'r') as fh:
            build_config = json.load(fh)

        build_zip(
            build_config['zip_file'],
            json_file.parent,
            build_config['files'],
            config)

    except (json.decoder.JSONDecodeError, KeyError):
        print(f"- Error parsing {json_file}")
        continue

