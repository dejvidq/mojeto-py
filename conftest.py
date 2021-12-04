import random
import string

import pytest

from mojeto.cli.init import Init

@pytest.fixture
def random_repo_name():
    repo_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return f"/tmp/{repo_name}"

@pytest.fixture
def generate_random_repo(random_repo_name):
    mojeto_init = Init(random_repo_name)
    mojeto_init.create_working_directory()
    return mojeto_init.repo_location
