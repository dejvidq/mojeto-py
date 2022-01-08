import yaml

from mojeto.utils.utils import decode_file_path
from .constants import CONFIG_PATH


class Config:

    def __init__(self):
        self.config_path = CONFIG_PATH
        self.config = self.open_config()
        if self.config[1]['files'] is None:
            self.config[1]['files'] = {}
        self.repo_location = self.config[0]['files_location']['path']

    def open_config(self) -> list:
        with open(self.config_path, "r") as conf_file:
            yaml_conf = yaml.safe_load(conf_file.read())
        return yaml_conf

    def add_file(self, file_name: str, file_path: str) -> None:
        self.config[1]['files'][file_name] = {
            "path": file_path
        }
        self.write_config()

    def write_config(self) -> None:
        with open(self.config_path, "w") as conf_file:
            conf_file.write(yaml.safe_dump(self.config))

    def get_all_files(self) -> dict[str, str]:
        files = {}
        for name, path in self.config[1]['files'].items():
            files[name] = path['path']
        return files

    def remove_file(self, name: str, path: str):
        if name in self.config[1]['files'].keys() and self.config[1]['files'][name]['path'] == path:
            del self.config[1]['files'][name]
            self.write_config()
        else:
            print(f"File {name} pointing to path '{decode_file_path(path)}' not found. Ommiting.")
