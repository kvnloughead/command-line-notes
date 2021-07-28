"""
Intended functionality
  1. listing all categories
  2. listing all tags
  3. listing notes found in category, or by tag
"""
import os

from parse import parse_show_args
from utils.constants import BASE_PATH

def show(args):
  kwargs = parse_show_args(args)
  for dirpath, subdirectories, filenames in os.walk(BASE_PATH):
    print(dirpath, subdirectories, filenames)
  