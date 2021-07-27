import shelve
from pathlib import Path

shelf = shelve.open('shelf')

def update_category_shelf(kwargs):
  """
  Adds category to the category shelf, and provides some protection against
  duplicated category pairs of the form thing|things.
  """
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



