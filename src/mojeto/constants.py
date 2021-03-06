import os
from pathlib import Path, PurePath


DEFAULT_CONFIG = """
- files_location:
    path: REPO_LOCATION
- files:
"""

CONFIG_PATH = str(PurePath(os.environ.get("MOJETO_CONFIG_LOCATION", str(PurePath(Path.home(), ".config", "mojeto"))),
                           ".mojeto"))
CONFIG_OVERRIDE_QUESTION = "Mojeto config already exist. Do you want to override it?"
