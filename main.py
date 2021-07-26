"""
Basic command line note-taking program. See individual action files for 
usage notes. This file parses the command line arguments and calls the
appropriate module.
"""

import sys

from utils.errors import MESSAGES
from edit import edit
from show import show

try: 
    [filename, action] = sys.argv[:2]
except ValueError:
    print(MESSAGES['missing action'])
    exit()
args = sys.argv[2:]

actions = {
    'edit': edit,
    'show': show,
}

if __name__ == '__main__':
    actions[action](args)
