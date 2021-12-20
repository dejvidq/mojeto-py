from pathlib import Path, PurePath
import shutil

from mojeto.config import Config
from mojeto.utils.utils import prompt_yes_no


class Apply:

    def __init__(self):
        self.config = Config()
        self.files = self.config.get_all_files()

    def __call__(self):
        if prompt_yes_no(question="Are you sure you want to override all files?"):
            for file, path in self.files.items():
                if Path(path).is_dir():
                    shutil.copy(src=Path(PurePath(self.config.repo_location, file)), dst=Path(PurePath(file, path)))
                elif prompt_yes_no(question=f"Path {path} does not exist. Do you want to create it?"):
                    # create path
                    p = Path(path)
                    p.mkdir(parents=True, exist_ok=True)
                    # copy file
                    shutil.copy(src=Path(PurePath(self.config.repo_location, file)), dst=Path(PurePath(file, path)))
                else:
                    print(f"Path {path} does not exist. Omitting")
