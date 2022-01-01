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
from opendir import opendir
from push import push
from commit import commit
from grep import grep
from find import find
from rename import rename

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(
    title="subcommands", description="", help="-"*10)

edit_parser = subparsers.add_parser(
    "edit",
    aliases=["e"],
    help="`cln edit foo` opens a note called `foo` for editing, creating it if it doesn't already exist")
edit_parser.add_argument(
    "name", nargs="?", help="the name of the note to be created/edited")
edit_parser.set_defaults(func=edit)

delete_parser = subparsers.add_parser(
    "delete",
    aliases=["d"],
    help="`cln delete foo` deletes a note called `foo`, if it exists. Prompts for confirmation.")
delete_parser.add_argument(
    "name",
    nargs="?",
    help="the name of the note to be deleted")
delete_parser.set_defaults(func=delete)

show_parser = subparsers.add_parser(
    "show",
    aliases=["s"],
    help="`cln show` prints a list of all notes to terminal")
show_parser.add_argument(
    "--pager", "-p", action="store_true", help="Pipes output of `cln show` to `less`.")
show_parser.set_defaults(func=show)

open_parser = subparsers.add_parser(
    "opendir",
    aliases=["o"],
    help="""`cln opendir` opens the notes directory in the editor.\n
        Currently this will only work if your default editor (found in 
        constants.py) accepts a directory as an argument.""")
open_parser.set_defaults(func=opendir)

push_parser = subparsers.add_parser(
    "push",
    aliases=["p"],
    help="runs `git add -A`, `git commit` and `git push` in your notes directory")
push_parser.set_defaults(func=push)

commit_parser = subparsers.add_parser(
    "commit",
    aliases=["c"],
    help="runs `git add -A` and `git commit` in your notes directory")
commit_parser.set_defaults(func=commit)

grep_parser = subparsers.add_parser(
    "grep",
    aliases=["g"],
    help="`cln grep foo` greps for `foo` in your notes directory")
grep_parser.add_argument("pattern", help="the pattern to be grepped for")
grep_parser.set_defaults(func=grep)

find_parser = subparsers.add_parser(
    "find",
    aliases=["f"],
    help="finds all files with similar names")
find_parser.add_argument(
    "pattern", help="the pattern to search for in the note names")
find_parser.set_defaults(func=find)

rename_parser = subparsers.add_parser(
    "rename",
    aliases="r",
    help="`cln r oldname newname` renames the given note")
rename_parser.add_argument(
    "oldname", help="the name of the note to be renamed")
rename_parser.add_argument(
    "newname", help="the new name for the note")
rename_parser.set_defaults(func=rename)


parser.add_argument("-c", "--category", help="specifies category of note; defaults to 'cheatsheet'",
                    default="default")
parser.add_argument("-t", "--tags", help="a comma separated list of tags",
                    default="")
parser.add_argument("-x", "--extension", help="extension of help file; defaults to .md",
                    default="md")
parser.add_argument("-a", "--author", help="author of the note -- this could be you!",
                    default=AUTHOR)
parser.add_argument(
    "-e", "--editor", help="specifies editor; defaults to code")
parser.add_argument("-m", "--micro", help="sets editor == micro",
                    action="store_const", const="micro")
parser.add_argument(
    "-dev", help="developer mode uses different directory for notes", action="store_true")

args = parser.parse_args()

if not "func" in args:
    parser.print_help()
    sys.exit()
else:
    args.func(args)
