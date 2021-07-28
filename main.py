"""
Basic command line note-taking program. See individual action files for 
usage notes. This file parses the command line arguments and calls the
appropriate module.
"""

import sys
import argparse

from utils.constants import AUTHOR
from utils.errors import MESSAGES
from edit import edit
from show import show

parser = argparse.ArgumentParser()

# parsers for subcommands
actions = parser.add_subparsers(title='available subcommands', dest='action',
                                metavar='action')

editParser = actions.add_parser('edit', help='opens new or existing note for editing')
editParser.add_argument('-n', '--name', help='the name of the note file')
editParser.add_argument('-c', '--category', help='specifies category of note; defaults to "default"',
                        default='default')
editParser.add_argument('-t', '--tags', help='specifies category of note; defaults to "default"',
                        default='')
editParser.add_argument('-e', '--extension', help='extension of help file; defaults to .md',
                       default='md')
editParser.add_argument('-a', '--author', help='author of the note -- this could be you!',
                        default=AUTHOR)

showParser = actions.add_parser('show', help="lists notes according to user supplied options")

args = parser.parse_args()

actions = {
    'edit': edit,
    'show': show,
}

if __name__ == '__main__':
    actions[args.action](args)
