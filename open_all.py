"""Opens the notes directory in editor."""

import os

from utils.constants import EDITOR, BASE_PATH

def open_all(args):
  os.system(f'{EDITOR} {BASE_PATH}')
  
