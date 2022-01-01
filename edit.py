"""Creates a new note or edits an existing note.

   Usage  
        $ python3 main.py edit note-name --category category-name 
                                         --tags comma,separated,tags
                                         
                                         
"""

import os
from pathlib import Path

from utils.constants import EDITOR, get_base_path
from utils.helpers import mkdir, create_new_note


def edit(args):
    """
    Opens note file for editing, creating it if it doesn't already exist.
    args: filename: string, category: string, tags: list of strings
    """
    editor = args.editor or args.micro or EDITOR
    BASE_PATH = get_base_path(args)
    mkdir(Path(BASE_PATH, args.category), BASE_PATH, args)
    path = Path(BASE_PATH, args.category, f"{args.name}.md")
    if not path.exists():
        path.write_text(create_new_note(args))
    os.system(f'{editor} {path}')
