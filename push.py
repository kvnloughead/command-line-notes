"""
Runs `git add -A`, `git commit` and `git push`. 

Assumes a certain amount of setup, like running `git init` and syncing to gh. TODO - elaborate

Always pushes to wherever you set the upstream repo. No support for anything fancy, like branches. But 
you can always run `cln -o` to open the directory in your editor and git to your heart's content.
"""

import os
from datetime import datetime

def push(args):
  default = f'update-notes: {datetime.now()}'
  message = str(input(f'\nCommit message (default = "{default}"):  '))
  message = message if message else default
  os.system(f'cd ~/.notes && git add -A && git commit -m "{message}" && git push')