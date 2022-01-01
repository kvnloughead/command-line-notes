"""
Runs `git add -A`, `git commit` and `git push` in your .notes directory (or 
`.notes-dev` you're if in dev mode (see docs/config.md for how to set options).

Always pushes to wherever you set the upstream repo. No support for anything
fancy, like branches. But you can always run `cln opendir` to open the directory
in your editor and git to your heart's content.

Current assumes a certain amount of setup has already taken place. Here are the
steps that are necessary prior to using `cln push`:
    
    1. run `git init` in `~/.notes`
    2. create a repo on GH to store the notes
    3. `git remote add origin main`
    4. `git push -u origin main`
    
If you are using dev mode, change `.notes` to `.dev-notes` and `main` to `dev`. It would be safer to use separate repos for production and development.
"""

import os
from datetime import datetime

from utils.constants import get_base_path
from commit import commit


def push(args):
    BASE_PATH = get_base_path(args)
    commit(args)
    remote_repo = 'dev' if args.dev else ''
    os.system(f'cd {BASE_PATH} && git push origin {remote_repo}')
