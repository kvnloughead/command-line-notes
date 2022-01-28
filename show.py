"""
Prints a list all your notes to the terminal, separated by category.
"""
import os

from utils.helpers import pipepager
from utils.constants import get_base_path
from utils.dotdict import dotdict


def get_categories(args):
    """Returns an array of dotdicts representing categories (name and path)"""
    BASE_PATH = get_base_path(args)
    files = [f for f in os.listdir(BASE_PATH) if f[0] != '.']  # ignore .git
    categories = [dotdict({'name': d, 'path': os.path.join(BASE_PATH, d)})
                  for d in files if os.path.isdir(os.path.join(BASE_PATH, d))]
    return categories


def generate_text(categories):
    """Returns text listing all notes, divided by category."""
    text = ''
    for c in categories:
        text += f'\nCategory -- {c.name}\n'
        text += f'============{"=" * len(c.name)}\n'
        for note in os.listdir(c.path):
            text += f'{note}\n'
        text += '\n'
    return text


def show(args):
    """Prints a human readable list of notes, separated into categories.
    If `args.pager`, the output is passed to `less`."""
    categories = get_categories(args)
    text = generate_text(categories)
    if (args.pager):
        pipepager(text, 'less')
    else:
        print(text)
