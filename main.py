"""
Basic command line note-taking program. See individual action files for 
usage notes. This file parses the command line arguments and calls the
appropriate module.
"""

import sys

from constants import OPTIONS, OPTION_DEFAULTS
from edit import edit

def parse_args(args):
    """
    Parses args, returning the first three arguments (including filename) as a list
    and the remaining arguments parsed into a dict of the form { 'option': value }.
    Example: 
    
        $ note edit -n curl -c cheatsheet -t bash,linux

    is parsed as ['main.py', 'edit', 'curl'], { 'category': 'cheatsheet', 'tags': 'bash,linux' }
    """
    if not args[2].startswith('-'): # make -name flag optional
        args.insert(2, '-name')
    options = [OPTIONS[arg.replace('-', '')] for arg in args[2::2]]
    kwargs = dict(zip(options, args[3::2]))
    kwargs = { **OPTION_DEFAULTS, **kwargs }
    return args[:2], kwargs

[filename, action], kwargs = parse_args(sys.argv)
print(kwargs)

actions = {
    'edit': edit(**kwargs),
}

if __name__ == '__main__':
    actions[action]
