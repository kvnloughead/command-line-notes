"""Creates new note or edits existing note.
   Usage  
        $ note edit note-name -category category-name 
                              -extension file-extension
                              -tags comma,separated,tags
"""

import os
from pathlib import Path

EDITOR = 'code'
BASE_PATH = Path(Path.home(), 'note-taker')

def edit(filename, category='default', extension='md', tags=[]):
    """
    Opens note file for editing, creating it if it doesn't already exist.
    args: filename: string, extension: string, category: string, tags: list of strings
    """
    path = Path(BASE_PATH, category, f'{filename}.{extension}')
    os.system(f'{EDITOR} {path}')  