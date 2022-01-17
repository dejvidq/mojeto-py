from pathlib import Path, PurePath
import shutil

from mojeto.constants import CONFIG_OVERRIDE_QUESTION, CONFIG_PATH, DEFAULT_CONFIG
from mojeto.utils.utils import prompt_yes_no


class Init:

    def __init__(self, location: str | Path) -> None:
        if not location:
            location = Path(CONFIG_PATH).parent
        self.repo_location = str(Path.resolve(Path(location)))
        self.config_path = CONFIG_PATH

    def __call__(self) -> None:
        if Path(self.repo_location).is_dir():
            if Path(CONFIG_PATH).is_file():
                if prompt_yes_no(question=CONFIG_OVERRIDE_QUESTION, default="no"):
                    if Path(PurePath(self.repo_location, ".mojeto")).is_file():
                        print("Nadpisanie i uzycie")
                        self.apply_config_from_repo()
                    else:
                        self.create_config_file(override=True)
            else:
                if Path(PurePath(self.repo_location, ".mojeto")).is_file():
                    print("uzycie")
                    self.apply_config_from_repo()
                else:
                    self.create_config_file()
        else:
            self.create_working_directory()
            self.create_config_file()

    def create_working_directory(self) -> None:
        path = Path(self.repo_location)
        path.mkdir(parents=True, exist_ok=True)

    def create_config_file(self, override: bool = False) -> None:
        content = DEFAULT_CONFIG.replace("REPO_LOCATION", self.repo_location)
        with open(PurePath(self.config_path), "w+") as conf:
            if override:
                conf.truncate()
            conf.write(content)

    def apply_config_from_repo(self) -> None:
        # zmiana repo_location w tym kopiowanym configu na ścieżkę podaną jako argument
        shutil.copy(src=PurePath(self.repo_location, ".mojeto"), dst=CONFIG_PATH)
