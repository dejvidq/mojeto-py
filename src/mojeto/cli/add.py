from pathlib import Path

from mojeto.config import Config
from mojeto.utils.utils import encode_file_path


class Add:

    def __init__(self) -> None:
        self.config = Config()

    def __call__(self, file_path: str) -> None:
        src_path = Path(file_path).resolve()
        if src_path.is_file():
            file_to_add_name = src_path.name
            file_to_add_path = encode_file_path(src_path)
            self.config.add_file(file_name=file_to_add_name, file_path=file_to_add_path)
        else:
            print(f"File {str(src_path)} does not exist. Omitting")
