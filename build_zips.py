#!/usr/bin/env python3

"""

This script builds zip files to be released to GitHub.

The zip files are only updated if the files are changed or renamed.

"""

import zipfile
import hashlib
from pathlib import Path


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


def build_zip(zip_name, root_path, paths):
    """
    TODO: document it
    """

    print(f'Checking {zip_name}')
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

    all_files.sort(key=lambda x: x[0])

    main_hash = hashlib.sha256()
    all_digests = []
    for file_pair in all_files:
        file_hash = hashlib.sha256()
        with open(file_pair[1], 'rb') as fh:
            file_hash.update(fh.read())

        file_digest = f'{file_pair[0]}:{file_hash.hexdigest()}\n'
        all_digests.append(file_digest)
        print(f'- {file_digest.strip()}')
        main_hash.update(file_digest.encode('utf-8'))

    new_digest = main_hash.hexdigest()
    all_digests.append(f'{zip_name}:{new_digest}')

    private_digest_file = Path('.' + zip_name.rsplit('.', 1)[0] + '.sha256')
    public_digest_file = Path(zip_name + '.sha256sum')

    if private_digest_file.is_file():
        with open(private_digest_file, 'r') as fh:
            old_digest = fh.read().strip().split('\n')[-1].split(':')[-1]

        if new_digest == old_digest:
            print('- File is up to date.')
            return

    print('- Building Zip')
    with zipfile.ZipFile(zip_name, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for file_pair in all_files:
            zf.write(file_pair[1], file_pair[0])

    print('- Recording sha256sum')
    final_hash = hashlib.sha256()
    with open(zip_name, 'rb') as fh:
        final_hash.update(fh.read())

    final_digest = final_hash.hexdigest()

    with open(public_digest_file, 'w') as fh:
        fh.write(f'{final_digest} *{Path(zip_name).name}')

    print('- Recording Digests')
    with open(private_digest_file, 'w') as fh:
        fh.write(''.join(all_digests))

# Fallout
build_zip(
    'releases/Fallout 1.zip',
    'Fallout 1', (
        'Fallout 1.sh',
        'fallout1',
        ('README.md', 'fallout1/README.md'),
        ('build', 'fallout1'),
        ))

# GemRB
build_zip(
    'releases/GemRB.zip',
    'GemRB', (
        'GemRB.sh',
        'gemrb',
        ('README.md', 'gemrb/README.md'),
        ('build', 'gemrb'),
        ))

# Half-Life
build_zip(
    'releases/Half-Life.zip',
    'Half-Life', (
        'Half-Life.sh',
        'Half-Life',
        ('README.md', 'Half-Life/README.md'),
        ('build', 'Half-Life', 1),
        ('build/valve', 'Half-Life/binaries/valve'),
        ('build/bshift', 'Half-Life/binaries/bshift'),
        ('build/gearbox', 'Half-Life/binaries/gearbox'),
        ))

# OpenRCT2
build_zip(
    'releases/OpenRCT2.zip',
    'OpenRCT2', (
        'OpenRCT2.sh',
        'openrct2',
        ('README.md', 'openrct2/README.md'),
        ('build', 'openrct2'),
        ))

# Rlvm
build_zip(
    'releases/Rlvm.zip',
    'Rlvm', (
        'Rlvm.sh',
        'rlvm',
        ('README.md', 'rlvm/README.md'),
        ('build', 'rlvm'),
        ))



