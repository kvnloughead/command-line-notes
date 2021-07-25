"""
Basic command line note-taking program. See individual action files for 
usage notes. This file parses the command line arguments and calls the
appropriate module.
"""

import sys

from constants import OPTIONS
from edit import edit

def parse_args(args):
    """
    Parses args, returning the first three arguments (including filename) as a list
    and the remaining arguments parsed into a dict of the form { 'option': value }.
    Example: 
    
        $ note edit curl -category cheatsheet -tags bash,linux

    is parsed as ['main.py', 'edit', 'curl'], { 'category': 'cheatsheet', 'tags': 'bash,linux' }
    """
    options = [OPTIONS[arg.replace('-', '')] for arg in args[3::2]]
    kwargs = dict(zip(options, args[4::2]))
    return args[:3], kwargs

[filename, action, name], kwargs = parse_args(sys.argv)

actions = {
    'edit': edit(name, **kwargs),
}

if __name__ == '__main__':
    actions[action]
    edit(name, **kwargs)
