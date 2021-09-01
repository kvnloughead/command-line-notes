from pathlib import Path

EDITOR = 'code'

def get_base_dir(args):
  return '.notes-dev' if args.dev else '.notes'
def get_base_path(args):
  return Path(Path.home(), get_base_dir(args))
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