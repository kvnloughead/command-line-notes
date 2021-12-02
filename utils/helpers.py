from pathlib import Path
import os


def mkdir(path, base_path, args, parents=True, exist_ok=False):
    try:
        Path(path).mkdir(parents=parents, exist_ok=exist_ok)
        if os.system(f'cd {base_path} && git rev-parse --is-inside-work-tree >/dev/null 2>&1'):
            os.system(f'cd {base_path} && git init')
        else:
            os.system(f'cd {base_path}')
    except FileExistsError:
        pass


def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(f'{question} (y/n): ')).lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            return False

# this works, but I'm not sure if it is an improvement


def create_subparser(name, action, options={}, arguments=[]):
    """
    `name` - the subparsers command
    `action` - the function to be called by the command
    `options` - a dict containing options to supply to subparser.add_parser
    `arguments` - a list of dicts containing args to be passed to add_argmunent
    """
    subparser = subparsers.add_parser(name, **options)
    for argument in arguments:
        subparser.add_argument(**argument)
    subparser.set_defaults(func=action)
    return subparser
