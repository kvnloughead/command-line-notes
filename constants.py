from pathlib import Path

EDITOR = 'code'
BASE_DIR = 'note-taker'
BASE_PATH = Path(Path.home(), BASE_DIR)

OPTIONS = {
    'c': 'category',
    'cat': 'category',
    'category': 'category',
    'e': 'extension',
    'ext': 'extension',
    'extensions': 'extension',
    't': 'tags',
    'tags': 'tags'
}