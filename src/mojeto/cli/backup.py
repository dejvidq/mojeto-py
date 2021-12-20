from pathlib import Path, PurePath
import shutil

from mojeto.config import Config


class Backup:

    def __init__(self):
        self.config = Config()

    def __call__(self):
        files_to_backup = self.config.get_all_files()
        for file, path in files_to_backup.items():
            file_path = Path(PurePath(path, file))
            if file_path.is_file():
                shutil.copy(src=file_path, dst=self.config.repo_location)
            else:
                print(f"File {file_path} does not exist. Omitting")
