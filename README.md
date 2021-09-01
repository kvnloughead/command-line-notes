# Command Line Notes

A simple command line note taking utility. It's like [tldr](https://github.com/tldr-pages/tldr) but without all the features, and it's completely empty until you start using it.


## Installation

1. Clone the repo into a directory that's in your PATH.
2. Open `~/.bashrc` and add the line `alias cln='python3 path/to/dir/main.py`. 
3. Restart bash, or source bashrc with `source ~/.bashrc`.

## Basic usage

```bash
cln foo
```

opens a file `foo.md`, creating it if it doesn't already exist. Note files are saved in a directory `~/.notes` and are subdivided by category. The default category is cheatsheet, and feel free to just use that. 

## Other Usage

```bash
cln -h                    # get help
cln -o                    # opens all your notes in your editor of choice
                          # you may need to set your EDITOR in .bashrc
cln foo -d                # deletes note named foo.md in default directory
cln -s                    # lists all notes and categories in terminal

```


## Git integration
This requires a bit of setup

## Development
If you'd like to work on this app yourself, you can run it with the `-dev` flag. This only changes the directory in which notes are placed to `~/.dev-notes`. Then you don't have to worry about messing up your actual notes. I keep two instances of the repo, one for prod and one for dev, and add the following to `~/.bashrc`:

```bash
alias cln='python3 path/to/prod/version/main.py'   # production version
alias clndv='python3 path/to/dev/version/main.py -dev' # development
```