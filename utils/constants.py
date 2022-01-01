from pathlib import Path
from config import settings

EDITOR = settings["EDITOR"] or 'nano'
AUTHOR = settings["AUTHOR"]


def get_base_dir(args):
    return '.notes-dev' if args.dev else '.notes'


def get_base_path(args):
    return Path(Path.home(), get_base_dir(args))
