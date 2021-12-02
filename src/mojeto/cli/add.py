from pathlib import Path

from mojeto.config import Config


class Add:

    def __init__(self) -> None:
        self.config = Config()

    def __call__(self, file_path) -> None:
        p = Path(file_path)
        name = p.name
        path = str(p.parents[0])
        self.config.add_file(file_name=name, file_path=path)
