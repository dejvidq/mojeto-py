import random
import string

import pytest

from src.mojeto.cli.init import Init


@pytest.fixture
def random_repo_name():
    repo_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return f"/tmp/{repo_name}"


@pytest.fixture
def generate_random_repo(random_repo_name):
    mojeto_init = Init(random_repo_name)
    mojeto_init.create_working_directory()
    return mojeto_init.repo_location


@pytest.fixture
def generate_random_repo_with_config(random_repo_name):
    mojeto_init = Init(random_repo_name)
    mojeto_init.create_working_directory()
    mojeto_init.create_config_file(config_path=f"{mojeto_init.repo_location}/.mojeto")
    return mojeto_init.repo_location
