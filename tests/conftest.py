import os
import random
import string

import pytest


@pytest.fixture
def repo_location():
    default_location = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    location = os.environ.get("MOJETO_CONFIG_LOCATION", f"/tmp/{default_location}")
    yield location
