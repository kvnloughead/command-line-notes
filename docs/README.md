# Command Line Notes

A simple command line note taking utility. It's like [tldr](https://github.com/tldr-pages/tldr) but without all the features, and it's completely empty until you start using it.


## Installation

1. Clone the repo into a directory that's in your PATH.[^1]
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
Local git integration should work out of the box. When you create your first commit, the `~/.notes` directory is initialized with `git init`. Then to make a commit, simply run `cln -c`. A default commit message with a timestamp will be provided, but you can override this if you'd like.

Github integration requires a few additional steps.

1. Create a new repo on Github.
2. Create a note and run `cln -c`.
3. Run `git remote add origin path/to/notes/repo` in your local notes directory to set the remote.
4. Run `cln -p` to push the `main` branch.

Now anytime you want to push, you just run `cln -p`.  

## Development
If you'd like to work on this app yourself, you can run it with the `-dev` flag. This only changes the directory in which notes are placed to `~/.notes-dev`. Then you don't have to worry about messing up your actual notes. I keep two instances of the repo, one for prod and one for dev, and add the following to `~/.bashrc`:

```bash
alias cln='python3 path/to/prod/version/main.py'   # production version
alias clndv='python3 path/to/dev/version/main.py -dev' # development
```

## Configuration
App configuration is handled by setting environmental variables in `settings.yaml`. Currently not many options are available, but more will be added. See ([./config.md](config.md).

## Dev Mode Git Integration
The first time a note is created with the `-dev` flag, the `.notes-dev` directory is initialized as a git repo and a `dev` branch is created and checked out. All commits and pushes made with the `-dev` flag will occur in this branch. 

To setup Github integration, you therefore need to follow the same steps with the `.notes-dev` directory. So you will wind up with two branches in your remote repo, with two separate local directories pointing to them.

[^1] To add a directory to your path, you can run `echo export PATH="path/to/dir:$PATH" > ~/.bashrc`.
