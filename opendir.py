"""Opens the notes directory in editor. If your chosen editor can't open directories, override it with `-e another-editor`."""

import os

from utils.constants import EDITOR, get_base_path


def opendir(args):
    BASE_PATH = get_base_path(args)
    os.system(f'{EDITOR} {BASE_PATH}')
