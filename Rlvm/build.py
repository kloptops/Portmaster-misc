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
with zipfile.ZipFile('Rlvm.zip', 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
    zf.write('Rlvm.sh')

    for src, dest in build_files(Path('rlvm'), 'rlvm'):
        print(src, dest)
        zf.write(str(src), str(dest))

    for src, dest in build_files(Path('build/'), 'rlvm'):
        print(src, dest)
        zf.write(str(src), str(dest))
