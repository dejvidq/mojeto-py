from pathlib import PurePath
import shutil

from mojeto.config import Config


class Backup:

    def __init__(self):
        self.config = Config()

    def __call__(self):
        files_to_backup = self.config.get_all_files()
        for file, path in files_to_backup.items():
            file_path = str(PurePath(path, file))
            shutil.copy(src=file_path, dst=self.config.repo_location)
