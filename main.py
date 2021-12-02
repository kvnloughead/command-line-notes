"""
Basic command line note-taking program. See individual action files for usage notes. 
This file parses the command line arguments and calls the appropriate module.

Usage
        cln note-name   # opens note called note-name.md
        cln -s          # shows all notes, organized by category
"""

import argparse
import sys

from utils.constants import AUTHOR
from edit import edit
from delete import delete
from show import show
from open_all import open_all
from push import push
from commit import commit
from grep import grep
from find import find

parser = argparse.ArgumentParser()

parser.add_argument('name', nargs='?', help='the name of the note file')

# used with `name` positional argument
parser.add_argument('-cat', '--category', help='specifies category of note; defaults to "cheatsheet"',
                    default='default')
parser.add_argument('-t', '--tags', help='a comma separated list of tags',
                    default='')
parser.add_argument('-x', '--extension', help='extension of help file; defaults to .md',
                    default='md')
parser.add_argument('-a', '--author', help='author of the note -- this could be you!',
                    default=AUTHOR)
parser.add_argument(
    '-d', '--delete', help='deletes the specified note', action='store_true')
parser.add_argument(
    '-e', '--editor', help='specifies editor; defaults to code')
parser.add_argument('-m', '--micro', help='sets editor == micro',
                    action='store_const', const='micro')
parser.add_argument(
    '-dev', help='developer mode uses different directory for notes', action='store_true')

# used without `name` positional argument
parser.add_argument(
    '-s', '--show', help='shows all notes; usage: `cln -s`', action='store_true')
parser.add_argument(
    '-o', '--openall', help='opens notes directory in editor', action='store_true')
parser.add_argument(
    '-p', '--push', help='runs git add, commit and push in your notes directory', action='store_true')
parser.add_argument(
    '-c', '--commit', help='runs git add and commit', action='store_true')
parser.add_argument(
    '-g', '--grep', help='greps notes; usage `cln -g foo` looks for "foo" inside all notes')
parser.add_argument(
    '-f', '--find', help='finds all files with similar names'
)


args = parser.parse_args()

if (not args.name):
    parser.print_help()
    sys.exit()
elif (args.show):
    action = show
elif (args.delete):
    action = delete
elif (args.openall):
    action = open_all
elif (args.push):
    action = push
elif (args.commit):
    action = commit
elif (args.grep):
    action = grep
elif (args.find):
    action = find
else:
    action = edit


if __name__ == '__main__':
    action(args)
