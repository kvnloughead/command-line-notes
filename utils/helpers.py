from pathlib import Path
import os

def mkdir(path, base_path, args, parents=True, exist_ok=False):
    try: 
        Path(path).mkdir(parents=parents, exist_ok=exist_ok)
        os.system(f'cd {base_path} && git init')
        if args.dev: os.system(f'cd {base_path} && git checkout -b dev')
    except FileExistsError: 
        pass

def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(f'{question} (y/n): ')).lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            return False