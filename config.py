from pathlib import Path
from dynaconf import Dynaconf

DYNACONF_SETTINGS_FILE = Path.home() / ".config" / "cln" / "settings.toml"
DYNACONF_SECRETS_FILE = Path.home() / ".config" / "cln" / ".secrets.toml"

settings = Dynaconf(
    environments=True,
    # makes production the default environment
    ENV_FOR_DYNACONF='production',
    envvar_prefix="CLN",
    load_dotenv=True,
    settings_files=[
        "settings.toml",        # defaults
        "settings.local.toml",  # user-defined
        DYNACONF_SETTINGS_FILE,  # also user-defined
        ".secrets.toml",
        ".secrets.local.toml",
        DYNACONF_SECRETS_FILE,
    ])

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `load_dotenv` = loads settings from `.env`
# `settings_files` = Load these files in the order
