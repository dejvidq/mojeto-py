import os
from pathlib import Path
import random
import shutil
import string

import pytest

from mojeto.cli.init import Init
from mojeto.constants import CONFIG_PATH


@pytest.fixture
def repo_name():
    repo_location = Path(CONFIG_PATH).parents[0]
    Path(repo_location).mkdir(parents=True, exist_ok=True)
    yield repo_location


@pytest.fixture
def generate_repo():
    mojeto_init = Init()
    mojeto_init.create_working_directory()
    yield mojeto_init.repo_location
    shutil.rmtree(mojeto_init.repo_location, ignore_errors=True)


@pytest.fixture
def generate_repo_with_config():
    mojeto_init = Init()
    mojeto_init.create_working_directory()
    mojeto_init.create_config_file(config_path=CONFIG_PATH)
    yield mojeto_init.repo_location
    shutil.rmtree(mojeto_init.repo_location, ignore_errors=True)


@pytest.fixture
def generate_repo_without_config():
    path = Path(CONFIG_PATH).parents[0]
    path.mkdir(parents=True, exist_ok=True)
    yield str(path)
    shutil.rmtree(str(path), ignore_errors=True)
