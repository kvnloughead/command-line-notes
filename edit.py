"""Creates new note or edits existing note.
   Usage  
        $ note edit note-name -category category-name 
                              -extension file-extension
                              -tags comma,separated,tags
"""

import os
from pathlib import Path
from datetime import date

from constants import EDITOR, BASE_PATH
from utils import mkdir

def edit(**kwargs):  
    """
    Opens note file for editing, creating it if it doesn't already exist.
    args: filename: string, extension: string, category: string, tags: list of strings
    """
    mkdir(Path(BASE_PATH, kwargs['category']))
    path = Path(BASE_PATH, kwargs['category'], f"{kwargs['name']}.{kwargs['extension']}")
    if not path.exists():
        path.write_text(create_new_note(**kwargs))
    os.system(f'{EDITOR} {path}')

def create_new_note(**kwargs):
    meta_data = [
        ['Title', kwargs['name']],
        ['Category', kwargs['category']],
        ['Author', kwargs['author'] ],
        ['Date', date.today()],
        ['Tags', kwargs['tags']]
    ]

    meta_data_string = '---  \n'
    for [key, value] in meta_data:
        meta_data_string += f"{key}: {value}  \n"
    meta_data_string += '---  \n'

    return meta_data_string