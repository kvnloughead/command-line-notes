## Git integration
Local git integration should work out of the box. When you create your first commit, the `~/.cln/notes` directory is initialized with `git init`. Then to make a commit, simply run `cln commit`. A default commit message with a timestamp will be provided, but you can override this if you'd like.

GitHub integration requires a few additional steps. Assuming that you've already created a note and made a commit, you then need to

1. Create a new repo on Github.
3. Run `git remote add origin path/to/remote/notes/repo` in your local notes directory to set the remote.
4. Run `cln push` to push the `main` branch.

Now anytime you want to push, you just run `cln push`.  