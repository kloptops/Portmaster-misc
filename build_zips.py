#!/usr/bin/env python3

"""

A crude script to put all the pieces together.

"""

import zipfile
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


def make_zip(zip_name, root_path, paths):
    """
    TODO: document it
    """
    if Path(zip_name).is_file():
        print(f"Skipping {zip_name}.")
        return

    print(f"Building {zip_name}.")
    with zipfile.ZipFile(zip_name, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in paths:
            max_depth = None
            if isinstance(path, (list, tuple)):
                if len(path) == 2:
                    real_name, internal_name = path
                elif len(path) == 3:
                    real_name, internal_name, max_depth = path
                else:
                    print(f"Bad path in paths, length of tuple must be 2 or 3: {path}")
                    continue
            else:
                real_name = internal_name = path

            full_name = Path(root_path) / real_name
            if full_name.is_file():
                print(f"- Adding {str(full_name)!r} as {str(internal_name)!r}")

                zf.write(str(full_name), str(internal_name))
            elif full_name.is_dir():
                for src, dest in build_files(full_name, internal_name, max_depth):
                    print(f"- Adding {str(src)!r} as {str(dest)!r}")

                    zf.write(str(src), str(dest))
            else:
                print(f"- {str(full_name)!r} doesnt exist, skipping.")

# Fallout
make_zip(
    'releases/Fallout 1.zip',
    'Fallout 1', (
        'Fallout 1.sh',
        'fallout1',
        ('README.md', 'fallout1/README.md'),
        ('build', 'fallout1'),
        ))

# GemRB
make_zip(
    'releases/GemRB.zip',
    'GemRB', (
        'GemRB.sh',
        'gemrb',
        ('README.md', 'gemrb/README.md'),
        ('build', 'gemrb'),
        ))

# Half-Life
make_zip(
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
make_zip(
    'releases/OpenRCT2.zip',
    'OpenRCT2', (
        'OpenRCT2.sh',
        'openrct2',
        ('README.md', 'openrct2/README.md'),
        ('build', 'openrct2'),
        ))

# Rlvm
make_zip(
    'releases/Rlvm.zip',
    'Rlvm', (
        'Rlvm.sh',
        'rlvm',
        ('README.md', 'rlvm/README.md'),
        ('build', 'rlvm'),
        ))
