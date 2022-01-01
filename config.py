from pathlib import Path
from dynaconf import Dynaconf

DYNACONF_SETTINGS_FILE = Path.home() / ".config" / "cln" / "settings.toml"
DYNACONF_SECRETS_FILE = Path.home() / ".config" / "cln" / ".secrets.toml"

settings = Dynaconf(
    envvar_prefix="CLN",
    load_dotenv=True,
    settings_files=[
        DYNACONF_SETTINGS_FILE,
        DYNACONF_SECRETS_FILE,
        "settings.toml",
        ".secrets.toml",
    ])

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `load_dotenv` = loads settings from `.env`
# `settings_files` = Load these files in the order. Only the first
