"""
Parses incoming command line arguments.
"""

from typing import cast
from utils.constants import OPTIONS, OPTION_DEFAULTS
from shelf import update_category_shelf

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
    update_category_shelf(kwargs)
    return kwargs

def parse_show_args(args):
    options = [OPTIONS[arg.replace('-', '')] for arg in args[::2]]
    kwargs = dict(zip(options, args[1::2]))
    return kwargs