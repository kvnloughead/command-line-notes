"""
Runs `git add -A` and `git commit` in your .notes directory (or .notes-dev if if in you're dev mode (see docs/config.md for how to set options)

Provides a default commit message "update-notes" plus a datestamp.

Commits are made to `dev` branch in development mode. Otherwise to `main`.
"""

import os
from datetime import datetime

from utils.constants import get_base_path


def commit(args):
    BASE_PATH = get_base_path(args)
    default = f'update-notes: {datetime.now()}'
    message = str(input(f'\nCommit message (default = "{default}"):  '))
    message = message if message else default
    os.system(f'cd {BASE_PATH} && git add -A && git commit -m "{message}"')
