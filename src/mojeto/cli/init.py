from pathlib import Path, PurePath
from mojeto.utils.utils import prompt_yes_no


class Init:

    DEFAULT_LOCATION = str(PurePath(Path.home(), "mojeto"))

    def __init__(self, location=DEFAULT_LOCATION):
        self.repo_location = Path.resolve(Path(location))

    def initialize(self):
        if Path(self.repo_location).is_dir():
            if Path(PurePath(self.repo_location, ".mojeto")).is_file():
                print("Folder already exist. Do you want to override its config file? (y/N)")
                if prompt_yes_no(default="no"):
                    self.create_config_file(truncate=True)
            else:
                self.create_config_file()
        else:
            self.create_working_directory()
            self.create_config_file()

    def create_working_directory(self):
        p = Path(self.repo_location)
        p.mkdir(parents=True, exist_ok=True)

    def create_config_file(self, content="", truncate=False):
        with open(PurePath(self.repo_location, ".mojeto"), "w+") as conf:
            if truncate:
                conf.truncate()
            conf.write(content)
