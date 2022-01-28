from pathlib import Path
from datetime import date
import os


def mkdir(path, base_path, args, parents=True, exist_ok=False):
    try:
        Path(path).mkdir(parents=parents, exist_ok=exist_ok)
        # os.system(f'cd {base_path} && git init')
        # if os.system(f'cd {base_path} && git rev-parse --is-inside-work-tree >/dev/null 2>&1'):
        #     os.system(f'cd {base_path} && git init')
        # else:
        #     os.system(f'cd {base_path}')
        # print(
        #     os.system(f'cd {base_path} && git rev-parse --show-toplevel 2>/dev/null'))
        # print(os.getcwd())
        print('base_path', base_path)
        # TODO - compare Path to string from os.system
        print(type(base_path))
        if os.system(f'cd {base_path} && git rev-parse --show-toplevel 2>/dev/null') != base_path:
            print('true')
            os.system(f'cd {base_path} && git init')
        else:
            print('false')
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


def pipepager(text, cmd):
    """Page through text by feeding it to another program.
    Source - https://hg.python.org/cpython/file/3.5/Lib/pydoc.py#l1450
    """
    import io
    import subprocess

    proc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE)
    try:
        with io.TextIOWrapper(proc.stdin, errors='backslashreplace') as pipe:
            try:
                pipe.write(text)
            except KeyboardInterrupt:
                # We've hereby abandoned whatever text hasn't been written,
                # but the pager is still in control of the terminal.
                pass
    except OSError:
        pass  # Ignore broken pipes caused by quitting the pager program.
    while True:
        try:
            proc.wait()
            break
        except KeyboardInterrupt:
            # Ignore ctl-c like the pager itself does.  Otherwise the pager is
            # left running and the terminal is in raw mode and unusable.
            pass
