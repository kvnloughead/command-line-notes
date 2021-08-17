from pathlib import Path

def mkdir(path, parents=True, exist_ok=False):
    try: 
        Path(path).mkdir(parents=parents, exist_ok=exist_ok)
    except FileExistsError: 
        pass

def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(f'{question} (y/n): ')).lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            return False