from pathlib import Path

def mkdir(path, parents=True, exist_ok=False):
    try: 
        Path(path).mkdir(parents=parents, exist_ok=exist_ok)
    except FileExistsError: 
        pass