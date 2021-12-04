from pathlib import Path, PurePath
import random
import string

import pytest


from mojeto.cli.init import Init
from mojeto.constants import CONFIG_PATH


class TestInit:

    def test_init_create_working_directory(self, random_repo_name):
        init_obj = Init(location=random_repo_name)
        init_obj.create_working_directory()
        assert Path(random_repo_name).is_dir()

    def test_init_create_config_file(self, generate_random_repo):
        repo_location = generate_random_repo
        config_file = Path(f"{repo_location}/.mojeto")
        global CONFIG_PATH
        mojeto_init_obj = Init(location=repo_location)
        mojeto_init_obj.create_config_file(config_path=config_file)
        assert config_file.is_file()
