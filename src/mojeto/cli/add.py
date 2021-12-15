from pathlib import Path
import shutil

from mojeto.config import Config


class Add:

    def __init__(self) -> None:
        self.config = Config()

    def __call__(self, file_path) -> None:
        src_path = Path(file_path)
        if src_path.is_file():
            file_to_add_name = src_path.name
            file_to_add_path = str(src_path.parents[0])
            shutil.copy(src=src_path, dst=self.config.repo_location)
            self.config.add_file(file_name=file_to_add_name, file_path=file_to_add_path)
        else:
            print(f"File {str(src_path)} does not exist. Omitting")
