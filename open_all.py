"""Opens the notes directory in editor."""

import os

from utils.constants import EDITOR, get_base_path

def open_all(args):
  BASE_PATH = get_base_path(args)
  os.system(f'{EDITOR} {BASE_PATH}')
  
