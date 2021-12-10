from pathlib import Path, PurePath

from mojeto.constants import CONFIG_OVERRIDE_QUESTION, CONFIG_PATH, DEFAULT_CONFIG
from mojeto.utils.utils import prompt_yes_no


class Init:

    def __init__(self, location=CONFIG_PATH) -> None:
        if not location:
            location = Path(CONFIG_PATH).parents[0]
        self.repo_location = str(Path.resolve(Path(location)))

    def __call__(self) -> None:
        if Path(self.repo_location).is_dir():
            if Path(PurePath(CONFIG_PATH)).is_file():
                if prompt_yes_no(question=CONFIG_OVERRIDE_QUESTION, default="no"):
                    self.create_config_file(override=True)
            else:
                self.create_config_file()
        else:
            self.create_working_directory()
            self.create_config_file()

    def create_working_directory(self) -> None:
        path = Path(self.repo_location)
        path.mkdir(parents=True, exist_ok=True)

    def create_config_file(self, override=False, config_path=CONFIG_PATH) -> None:
        content = DEFAULT_CONFIG.replace("REPO_LOCATION", self.repo_location)
        with open(PurePath(config_path), "w+") as conf:
            if override:
                conf.truncate()
            conf.write(content)
