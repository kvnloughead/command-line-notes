# Settings

## Introduction
Settings can be added to either a file at `~/.config/cln/settings.toml`, or `settings.toml` at the root of the repo. Create the file if it doesn't exist. You can also override settings by adding them to a `.env` file in the project repo. When doing this, you must prefix the environmental variables with `CLN_` and use uppercase, like so:

```
CLN_DEV=True
```

`author` - the default author of notes. Maybe it could be useful for someone. Can be overridden with `cln edit -a "author name"`. Defaults to an empty string.

`editor` - your editor of choice. This can be overridden at run time with the `-e` flag. Example `cln edit -e vim`. Defaults to `nano`.

`dev` - Set to `True` to run `cln` in development mode. Basically this just sends notes to a different notes file and repo. I keep separate repos, one for personal use and one for development, adding `CLN_DEV=True` to a `.env` file in the latter.