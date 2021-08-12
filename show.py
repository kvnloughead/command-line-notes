"""
Intended functionality
  1. listing all categories
  2. listing all tags
  3. listing notes found in category, or by tag
"""
import os

from utils.constants import BASE_PATH
from utils.dotdict import dotdict

def show(args):
  files = [f for f in os.listdir(BASE_PATH) if f[0] != '.']
  categories = [dotdict({'name': d, 'path': os.path.join(BASE_PATH, d)}) for d in files if os.path.isdir(os.path.join(BASE_PATH, d))]
  for c in categories:
    print(f'\nCategory -- {c.name}')
    print(f'============{"=" * len(c.name)}')
    for note in os.listdir(c.path):
      print(note)
    print('\n')