import os
from pathlib import Path
from utils.constants import EDITOR, get_base_path


def grep(args):
    BASE_PATH = get_base_path(args)
    os.system(
        f'''grep -r --color --exclude-dir=.git {args.pattern} {BASE_PATH} || echo "no matching notes"
        ''')
