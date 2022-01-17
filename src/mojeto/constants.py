from pathlib import Path, PurePath


DEFAULT_CONFIG = """
- files_location:
    path: REPO_LOCATION
- files:
"""

CONFIG_PATH = PurePath(Path.home(), ".config", "mojeto", ".mojeto").as_posix()
CONFIG_OVERRIDE_QUESTION = "Mojeto config already exist. Do you want to override it?"
