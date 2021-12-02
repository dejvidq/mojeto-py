import yaml

from .constants import CONFIG_PATH


class Config:

    def __init__(self):
        self.config_path = CONFIG_PATH
        self.config = self.open_config()
        if self.config[1]['files'] is None:
            self.config[1]['files'] = {}

    def open_config(self) -> list:
        with open(self.config_path, "r") as conf_file:
            yaml_conf = yaml.safe_load(conf_file.read())
        return yaml_conf

    def add_file(self, file_name, file_path) -> None:
        self.config[1]['files'][file_name] = {
            "path": file_path
        }
        self.write_config()

    def write_config(self) -> None:
        with open(self.config_path, "w") as conf_file:
            conf_file.write(yaml.safe_dump(self.config))
