from pathlib import Path
from datetime import date
import os


def mkdir(path, base_path, args, parents=True, exist_ok=False):
    try:
        Path(path).mkdir(parents=parents, exist_ok=exist_ok)
        if os.system(f'cd {base_path} && git rev-parse --is-inside-work-tree >/dev/null 2>&1'):
            os.system(f'cd {base_path} && git init')
        else:
            os.system(f'cd {base_path}')
    except FileExistsError:
        pass


def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(f'{question} (y/n): ')).lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            return False


def create_new_note(args):
    meta_data = [
        ['Title', args.name],
        ['Category', args.category],
        ['Author', args.author],
        ['Date', date.today()],
        ['Tags', args.tags]
    ]

    meta_data_string = '---  \n'
    for [key, value] in meta_data:
        meta_data_string += f"{key}: {value}  \n"
    meta_data_string += '---  \n'

    return meta_data_string
