from pathlib import Path

from mojeto.config import Config


class Add:

    def __init__(self) -> None:
        self.config = Config()

    def __call__(self, file_path) -> None:
        src_path = Path(file_path).resolve()
        if src_path.is_file():
            file_to_add_name = src_path.name
            file_to_add_path = self.prepare_file_path(src_path)
            self.config.add_file(file_name=file_to_add_name, file_path=file_to_add_path)
        else:
            print(f"File {str(src_path)} does not exist. Omitting")

    def prepare_file_path(self, src_path: Path):
        path = src_path.parents[0]
        home = Path.home()
        if home in src_path.parents:
            path = Path(src_path.parents[0].as_posix().replace(home.as_posix(), "%HOME%", 1))
        return path.as_posix()
