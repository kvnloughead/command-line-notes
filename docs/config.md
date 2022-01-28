# Settings

## Introduction
Settings can be added to either a file at `~/.config/cln/settings.toml`, or `settings.toml` at the root of the repo. Create the file if it doesn't exist. You can also override settings by adding them to a `.env` file in the project repo. When doing this, you must prefix the environmental variables with `CLN_` and use uppercase, like so:

```
CLN_ENV=dev
```

Most options can be overridden at run time with a the appropriate flag.

## Available Options

`author` - the default author of notes. Maybe it could be useful for someone. Can be overridden with the `-a` flag. Defaults to an empty string.

`editor` - your editor of choice. This can be overridden at run time with the `-e` flag. Example `cln edit -e vim`. Defaults to `nano`. Since `nano` cannot open directories, the `opendir` command won't work by default, opening a file called `.notes` inside your user directory. To fix this, override the editor with `-e another-editor`.

`env` - the environment to run the app in. By default this is `prod`. If you want to work on this app, you can set `CLN_ENV=dev` in `.env` (or `env = 'dev'` in `settings.toml`). Tests use `env = test`.

The main difference between the different environments is the location that the notes are stored in (locally, and on GitHub). These are `~/.cln/notes`, `~/.cln/notes-dev` and `tests/.notes-test` for `prod`, `dev` and `test` respectively.
