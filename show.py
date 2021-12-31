"""
Intended functionality
  1. listing all categories
  2. listing all tags
  3. listing notes found in category, or by tag
"""
import os

from utils.helpers import pipepager
from utils.constants import get_base_path
from utils.dotdict import dotdict


def show(args):
    BASE_PATH = get_base_path(args)
    files = [f for f in os.listdir(BASE_PATH) if f[0] != '.']
    categories = [dotdict({'name': d, 'path': os.path.join(BASE_PATH, d)})
                  for d in files if os.path.isdir(os.path.join(BASE_PATH, d))]
    text = ''
    for c in categories:
        text += f'\nCategory -- {c.name}\n'
        text += f'============{"=" * len(c.name)}\n'
        for note in os.listdir(c.path):
            text += f'{note}\n'
        text += '\n'
    if (args.pager):
        pipepager(text, 'less')
    else:
        print(text)
