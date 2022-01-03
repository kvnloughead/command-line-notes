"""
Basic command line note-taking program. See individual action files for usage notes.
This file parses the command line arguments and calls the appropriate module.

Usage
        cln note-name   # opens note called note-name.md
        cln -s          # shows all notes, organized by category
"""

from pathlib import Path
import argparse
import sys
import os

from utils.constants import AUTHOR, EDITOR
from edit import edit
from delete import delete
from show import show
from opendir import opendir
from push import push
from commit import commit
from grep import grep
from find import find
from rename import rename

os.environ['SETTINGS_FILE_FOR_DYNACONF'] = f'{Path.home()}/config/default.toml, <abs_path>/config1/settings.toml'


def parse_args(args):

    # main parser
    parser = argparse.ArgumentParser()

    # top level args
    parser.add_argument(
        "-dev", help="Developer mode uses different directory for notes.", action="store_true", default=False)
    parser.add_argument(
        "-test", help="Runs app in test mode. Used solely in the testing suite.", action="store_true", default=False
    )

    # parent parser with `e|editor` flag
    editor_parent_parser = argparse.ArgumentParser(add_help=False)
    editor_parent_parser.add_argument(
        "-e", "--editor", help="specifies editor; defaults to nano", default=EDITOR)

    # parent parser for metadata related options
    metadata_parent_parser = argparse.ArgumentParser(add_help=False)
    metadata_parent_parser.add_argument("-c", "--category", help="Specifies category of the note. Notes are organized into directories based on their category. Defaults to 'defaultmetadata_parent_'",
                                        default="default")
    metadata_parent_parser.add_argument("-t", "--tags", help="A comma separated list of tags.",
                                        default="")
    metadata_parent_parser.add_argument("-a", "--author", help="The author of the note.",
                                        default=AUTHOR)

    subparsers = parser.add_subparsers(
        title="subcommands", description="", help="-"*10)

    edit_parser = subparsers.add_parser(
        "edit",
        aliases=["e"],
        parents=[editor_parent_parser, metadata_parent_parser],
        help="`cln edit foo` opens a note called `foo` for editing, creating it if it doesn't already exist")
    edit_parser.add_argument(
        "name", nargs="?", help="the name of the note to be created/edited")
    edit_parser.set_defaults(func=edit)

    delete_parser = subparsers.add_parser(
        "delete",
        aliases=["d"],
        parents=[metadata_parent_parser],
        help="`cln delete foo` deletes a note called `foo`, if it exists. Prompts for confirmation.")
    delete_parser.add_argument(
        "name",
        nargs="?",
        help="the name of the note to be deleted")
    delete_parser.set_defaults(func=delete)

    show_parser = subparsers.add_parser(
        "show",
        aliases=["s"],
        help="`cln show` prints a list of all notes to terminal",
        parents=[metadata_parent_parser])
    show_parser.add_argument(
        "--pager", "-p", action="store_true", help="Pipes output of `cln show` to `less`.")
    show_parser.set_defaults(func=show)

    open_parser = subparsers.add_parser(
        "opendir",
        aliases=["o"],
        parents=[editor_parent_parser],
        help="""`cln opendir` opens the notes directory in the editor.\n
            Currently this will only work if your default editor (found in 
            constants.py) accepts a directory as an argument.""")
    open_parser.set_defaults(func=opendir)

    push_parser = subparsers.add_parser(
        "push",
        aliases=["p"],
        help="Runs `git add -A`, `git commit` and `git push` in your notes directory.\nRunning `cln` with the `-dev` flag changes the directory and repo.")
    push_parser.set_defaults(func=push)

    commit_parser = subparsers.add_parser(
        "commit",
        aliases=["c"],
        help="Runs `git add -A` and `git commit` in your notes directory. \nRunning `cln` with the `-dev` flag changes the directory and repo.")
    commit_parser.set_defaults(func=commit)

    grep_parser = subparsers.add_parser(
        "grep",
        aliases=["g"],
        parents=[metadata_parent_parser],
        help="`cln grep foo` greps for `foo` in your notes directory.")
    grep_parser.add_argument("pattern", help="the pattern to be grepped for")
    grep_parser.set_defaults(func=grep)

    find_parser = subparsers.add_parser(
        "find",
        aliases=["f"],
        help="`cln find foo` finds all files with the pattern `foo` in their filename.")
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

    return parser, parser.parse_args(args)


if __name__ == "__main__":
    parser, args = parse_args(sys.argv[1:])
    if not "func" in args:
        parser.print_help()
        sys.exit()
    else:
        args.func(args)
