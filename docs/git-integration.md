## Git integration
Local git integration should work out of the box. When you create your first commit, the `~/.notes` directory is initialized with `git init`. Then to make a commit, simply run `python3 main.py commit`. A default commit message with a timestamp will be provided, but you can override this if you'd like.

GitHub integration requires a few additional steps.

1. Create a new repo on Github.
2. Create a note and run `cln -c`.
3. Run `git remote add origin path/to/notes/repo` in your local notes directory to set the remote.
4. Run `cln -p` to push the `main` branch.

Now anytime you want to push, you just run `python3 main.py push`.  