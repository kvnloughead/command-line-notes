"""Deletes the specified note.
   Usage  
        $ cln note-name -d -c category-name  
"""

import os
from pathlib import Path

from utils.constants import get_base_path
from utils.helpers import yes_or_no


def delete(args):
    """Deletes the specified note."""
    BASE_PATH = get_base_path(args)
    path = Path(BASE_PATH, args.category, f"{args.name}.{args.extension}")
    if not path.exists():
        print(
            f'\nThere is no note called "{args.name}" with category "{args.category}"\n')
    else:
        question = f'\nDelete {args.name} from category {args.category}?'
        if yes_or_no(question):
            print('Note deleted')
            os.remove(path)
