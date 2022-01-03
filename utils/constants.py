import os
from pathlib import Path
from config import settings

EDITOR = settings.editor
AUTHOR = settings.author


def get_env(args):
    """Returns the current environment, either production, testing
    or development. Uses both command line flags and dynaconf env
    variables."""
    if args.dev or settings.env_for_dynaconf == 'development':
        return 'development'
    elif args.test or settings.env_for_dynaconf == 'testing':
        return 'testing'
    else:
        return 'production'


def get_base_path(args):
    """Returns the base path for your current environment. Environment can by changed with command line flags, or with environmental variables. 

    Notes for testing are stored in this repo, in the tests/ directory, because they are necessary for the tests. Other notes are stored in `~/.cln/`. 
    """
    ENV = get_env(args)
    base_dir = 'notes' if ENV == 'production' else f'notes-{ENV}'
    if ENV == 'testing':
        return Path(os.getcwd(), 'tests', base_dir)
    return Path(Path.home(), '.cln', base_dir)
