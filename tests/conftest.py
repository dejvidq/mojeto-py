import random
import shutil
import string

import pytest

from mojeto.cli.init import Init


@pytest.fixture
def random_repo_name():
    repo_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    repo_path = f"/tmp/{repo_name}"
    yield repo_path
    shutil.rmtree(repo_path, ignore_errors=True)


@pytest.fixture
def generate_random_repo(random_repo_name):
    mojeto_init = Init(random_repo_name)
    mojeto_init.create_working_directory()
    yield mojeto_init.repo_location
    shutil.rmtree(mojeto_init.repo_location, ignore_errors=True)


@pytest.fixture
def generate_random_repo_with_config(random_repo_name):
    mojeto_init = Init(random_repo_name)
    mojeto_init.create_working_directory()
    mojeto_init.create_config_file(config_path=f"{mojeto_init.repo_location}/.mojeto")
    yield mojeto_init.repo_location
    shutil.rmtree(mojeto_init.repo_location, ignore_errors=True)
