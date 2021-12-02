from pathlib import Path, PurePath
from mojeto.utils.utils import prompt_yes_no
from mojeto.constants import DEFAULT_CONFIG, CONFIG_PATH, CONFIG_OVERRIDE_QUESTION


class Init:

    def __init__(self, location=None):
        if not location:
            location = Path(CONFIG_PATH).parents[0]
        self.repo_location = str(Path.resolve(Path(location)))

    def __call__(self):
        if Path(self.repo_location).is_dir():
            if Path(PurePath(self.repo_location, ".mojeto")).is_file():
                if prompt_yes_no(question=CONFIG_OVERRIDE_QUESTION, default="no"):
                    self.create_config_file(override=True)
            else:
                self.create_config_file()
        else:
            self.create_working_directory()
            self.create_config_file()

    def create_working_directory(self):
        path = Path(self.repo_location)
        path.mkdir(parents=True, exist_ok=True)

    def create_config_file(self, override=False):
        content = DEFAULT_CONFIG.replace("REPO_LOCATION", self.repo_location)
        with open(PurePath(CONFIG_PATH), "w+") as conf:
            if override:
                conf.truncate()
            conf.write(content)
