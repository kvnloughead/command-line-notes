"""
Basic command line note-taking program. See individual action files for usage notes. 
This file parses the command line arguments and calls the appropriate module.

Usage
        cln note-name   # opens note called note-name.md
        cln -s          # shows all notes, organized by category
"""

import argparse

from utils.constants import AUTHOR
from edit import edit
from show import show

parser = argparse.ArgumentParser()

parser.add_argument('name', nargs='?', help='the name of the note file')
parser.add_argument('-c', '--category', help='specifies category of note; defaults to "cheatsheet"',
                        default='cheatsheet')
parser.add_argument('-t', '--tags', help='a comma separated list of tags',
                        default='')
parser.add_argument('-e', '--extension', help='extension of help file; defaults to .md',
                       default='md')
parser.add_argument('-a', '--author', help='author of the note -- this could be you!',
                        default=AUTHOR)
parser.add_argument('-s', '--show', help='shows all notes; usage: `cln -s`', action='store_true')

args = parser.parse_args()

if (args.show):
    action = show
else:
    action = edit


if __name__ == '__main__':
    action(args)
