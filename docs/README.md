# Command Line Notes

A simple command line note taking utility. Using the suggested aliases, you can create new markdown note files, or edit existing ones, with `cln edit note-name`. Notes are stored locally in `~/.notes` and are opened in the editor of your choice (defaults to `nano`. See [config.md](config.md) for details on how to change the defaults). Subcommands exist for 

- renaming and deleting notes
- grepping through the content of your notes
- finding notes that match a pattern
- printing a list of all notes to the terminal, or to a pager
- opening the directory of notes in your editor of choice
- pushing your notes to a remote repo (see [git-integration.md](./git-integration.md) for details)

## Installation

1. Clone the repo.
2. Open `~/.bashrc` and add the line `alias cln='python3 path/to/dir/main.py`. 
3. Restart bash, or source bashrc with `source ~/.bashrc`.

Now you should be able to run the program using the command `cln [args]` rather than `python3 path/to/main.py [args]`.

If you don't want to use `nano` as your editor, you can change this quite easily. Simply add the line `editor = 'your-editor'` to `~/.config/cln/settings.toml. See [config.md](config.md).

## Basic usage

```bash
cln edit foo
```

opens a file called `foo.md`, creating it if it doesn't already exist. Note files are saved in a directory `~/.notes` and are subdivided by category. The default category is `default`, and feel free to just use that. Notes are opened in your default editor.

Note that most subcommands have an obvious alias. For example, the `edit` command has an alias of `e`. I will use the notation `edit|e` to indicate these pairs.

## Other Usage

```bash
cln -h                    # gets help

cln delete|d foo          # deletes note named foo.md in default directory
cln edit|e foo            # creates/opens note called foo.md for editing
cln rename|r foo bar      # renames note called `foo.md` to `bar.md`

cln find foo              # finds all notes with name containing `foo`
cln grep pattern          # greps for the supplied pattern in your notes directory
cln show|s                # lists all notes and categories in terminal

cln commit|c              # runs `git add -A` and `git commit` in your notes file
                          # supplies a default commit message with timestamp
cln push|p                # runs `git add -A` and `git commit` in your notes file
                          # supplies a default commit message with timestamp                          

cln opendir|o             # opens all your notes in your editor of choice
                          # since the default editor is nano, this won't work out of the box
```


## Development
If you'd like to work on this app yourself, set `DEV=True` in the config file, or in `.env`. In `.env`, you must prefix variables with `CLN_`. So you would use `CLN_DEV=True`. When in dev mode, notes are saved in a different directory (`~/.notes-dev`) and are pushed to the `dev` branch instead of `main`. So you can work on the app without messing with your personal notes. 

Note that you can also work in dev mode by adding the `-dev` flag.

## Configuration
App configuration is handled by setting environmental variables in `settings.yaml`. Currently not many options are available, but more will be added. See ([./config.md](config.md).
