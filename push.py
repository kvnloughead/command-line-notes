"""
Runs `git add -A`, `git commit` and `git push` in your .notes directory 
(or .notes-dev if in -dev mode). 

Assumes a certain amount of setup, like running `git init` and syncing to gh. TODO - elaborate

Always pushes to wherever you set the upstream repo. No support for anything fancy, like branches. But 
you can always run `cln -o` to open the directory in your editor and git to your heart's content.
"""

import os
from datetime import datetime

from utils.constants import get_base_path
from commit import commit

def push(args):
  BASE_PATH = get_base_path(args)
  commit(args)
  os.system(f'cd {BASE_PATH} && git push' + ' origin dev' if args.dev else '')