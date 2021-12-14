import os
from pathlib import Path
import random
import shutil
import string

import pytest
from mojeto.cli.init import Init


@pytest.fixture
def repo_location():
    default_location = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    location = os.environ.get("MOJETO_CONFIG_LOCATION", f"/tmp/{default_location}")
    yield location
    shutil.rmtree(path=location, ignore_errors=True)


@pytest.fixture
def repo_location_created():
    default_location = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    location = os.environ.get("MOJETO_CONFIG_LOCATION", f"/tmp/{default_location}")
    path = Path(location)
    path.mkdir(parents=True, exist_ok=True)
    yield location
    shutil.rmtree(path=location, ignore_errors=True)


@pytest.fixture
def repo_location_created_with_config():
    default_location = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    location = os.environ.get("MOJETO_CONFIG_LOCATION", f"/tmp/{default_location}")
    path = Path(location)
    path.mkdir(parents=True, exist_ok=True)
    with open(f"{str(path)}/.mojeto", "w+") as _:
        pass
    yield location
    shutil.rmtree(path=location, ignore_errors=True)


@pytest.fixture
def init():
    init = Init(location='')
    init()
    yield
    shutil.rmtree(path=init.repo_location, ignore_errors=True)


@pytest.fixture
def tmp_file():
    file_name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    file = f"/tmp/{file_name}"
    with open(file, "w+") as _:
        pass
    yield file
    os.remove(file)
