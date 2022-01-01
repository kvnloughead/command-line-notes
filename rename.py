import re
import os
from pathlib import Path

from utils.constants import EDITOR, get_base_path
from utils.helpers import create_new_note


def rename(args):
    base_path = get_base_path(args)
    old_path = Path(base_path, args.category,
                    f'{args.oldname}.md')
    if not old_path.exists():
        print(
            f'There is no note called {args.oldname} in the {args.category} category.')
        return

    # if note exists, grab its contents and change the title field
    with open(Path(base_path, args.category, f'{args.oldname}.md'), 'r') as file:
        text = file.read()
    text = re.sub(r'Title: (.*)\n', f'Title: {args.newname}\n', text)

    # if possible, create new note with the updated content
    new_path = Path(base_path, args.category,
                    f'{args.newname}.md')
    if new_path.exists():
        print(f'There is already a note called {args.newname}')
        return
    else:
        os.rename(old_path, new_path)
        new_path.write_text(text)

    # TODO - delete file
