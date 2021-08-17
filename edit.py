"""Creates new note or edits existing note.
   Usage  
        $ note edit note-name --category category-name 
                              --extension file-extension
                              --tags comma,separated,tags
"""

import os
from pathlib import Path
from datetime import date

from utils.constants import EDITOR, BASE_PATH
from utils.helpers import mkdir

def edit(args):  
    """
    Opens note file for editing, creating it if it doesn't already exist.
    args: filename: string, extension: string, category: string, tags: list of strings
    """
    mkdir(Path(BASE_PATH, args.category))
    path = Path(BASE_PATH, args.category, f"{args.name}.{args.extension}")
    if not path.exists():
        path.write_text(create_new_note(args))
    os.system(f'{EDITOR} {path}')

    
def create_new_note(args):
    meta_data = [
        ['Title', args.name],
        ['Category', args.category],
        ['Author', args.author],
        ['Date', date.today()],
        ['Tags', args.tags]
    ]

    meta_data_string = '---  \n'
    for [key, value] in meta_data:
        meta_data_string += f"{key}: {value}  \n"
    meta_data_string += '---  \n'

    return meta_data_string