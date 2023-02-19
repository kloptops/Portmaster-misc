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

valid = False
with zipfile.ZipFile('Half-Life.zip', 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
    zf.write('Half-Life.sh')

    for src, dest in build_files(Path('Half-Life'), 'Half-Life'):
        print(src, dest)
        zf.write(str(src), str(dest))

    for src, dest in build_files(Path('build/'), 'Half-Life', max_depth=1):
        print(src, dest)
        zf.write(str(src), str(dest))

    for folder in ['valve', 'bshift', 'gearbox']:
        folder_root = Path('build') / folder
        folder_dest = Path('Half-Life/binaries') / folder
        if folder_root.is_dir():
            if folder == 'valve':
                # Pure jank
                valid = True
            for src, dest in build_files(folder_root, folder_dest):
                print(src, dest)
                zf.write(str(src), str(dest))

if not valid:
    print("No 'valve' build folder found, this is not a valid 'Half-Life.zip', deleting zip file.")
    Path('Half-Life.zip').unlink()
