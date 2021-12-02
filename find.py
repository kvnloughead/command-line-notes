import os
import textwrap
from pathlib import Path
from utils.constants import EDITOR, get_base_path


def find(args):
    foundSomething = False
    BASE_PATH = get_base_path(args)
    for root, dirs, files in os.walk(BASE_PATH):
        category = root.split('/')[-1]
        files = [f for f in files if not f[0] == '.']
        dirs[:] = [d for d in dirs if not d[0] == '.']
        found = [f for f in files if args.pattern in f]
        if len(found) > 0:
            foundSomething = True
            print(f'\n{category}')
            print('\n'.join([f'\t{f}' for f in found]))
            print("\n" + "=" * 40 + "\n")
    if not foundSomething:
        print("nothing found")
