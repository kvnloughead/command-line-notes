from pathlib import Path

EDITOR = 'code'
BASE_DIR = 'note-taker'
BASE_PATH = Path(Path.home(), BASE_DIR)
AUTHOR = 'Kevin Loughead'

OPTIONS = {
    'n': 'name',
    'name': 'name',
    'c': 'category',
    'cat': 'category',
    'category': 'category',
    'e': 'extension',
    'ext': 'extension',
    'extensions': 'extension',
    't': 'tags',
    'tags': 'tags',
    'a': 'author',
    'author': 'author',
}

OPTION_DEFAULTS = {
  'category': 'default',
  'extension': 'md',
  'author': f'{AUTHOR}',
  'tags': '',
}