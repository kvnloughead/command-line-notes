"""
Parses incoming command line arguments.
"""

from typing import cast
from utils.constants import OPTIONS, OPTION_DEFAULTS
from shelf import shelf

def parse_edit_args(args):
    """
    Parses options and other args into key-value pairs. Example:
    
        $ note edit -n curl -c cheatsheet -t bash,linux

    is parsed as { 'name': 'curl', 'category': 'cheatsheet', 'tags': 'bash,linux' }
    Notes:
        1. all options have valid forms -w|-word, and multiple hyphens are fine too
        2. if -n isn't included, it will be assumed
    """
    if not args[0].startswith('-'): 
        args.insert(0, '-name')                 # make -name flag optional
    options = [OPTIONS[arg.replace('-', '')] for arg in args[::2]]
    kwargs = dict(zip(options, args[1::2]))
    kwargs = { **OPTION_DEFAULTS, **kwargs }    # update kwargs with defaults

    # initialize shelf['category'] if necessary
    if 'category' not in shelf.keys():
        shelf['category'] = [] 
    # attempt to prevent proliferation of category pairs differing only in plurality
    if not kwargs['category'].endswith('s') and f"{kwargs['category']}s" in shelf['category']:
        ans = input(f"Did you mean \"{kwargs['category']}s\"? Yes or No\n")
        if ans.lower().startswith('y'):
            kwargs['category'] = f"{kwargs['category']}s"
    # add category to shelf
    shelf['category'] = list(set(shelf['category'] + [kwargs['category']]))

    return kwargs