from pathlib import Path, PurePath

from mojeto.config import Config
from mojeto.utils.utils import encode_file_path


class Remove:

    def __init__(self):
        self.config = Config()

    def __call__(self, file_path: str):
        src_path = Path(file_path).resolve()
        filename = src_path.name
        path = encode_file_path(src_path=src_path)
        self.config.remove_file(name=filename, path=path)
        try:
            Path(PurePath(self.config.repo_location, filename)).unlink()
        except FileNotFoundError:
            pass
