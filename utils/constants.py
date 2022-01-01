from pathlib import Path
from config import settings

EDITOR = settings.get('editor', 'nano')
AUTHOR = settings.get('author', '')
DEV = settings.get('dev', False)


def get_base_dir(args):
    return '.notes-dev' if DEV else '.notes'


def get_base_path(args):
    return Path(Path.home(), get_base_dir(args))
