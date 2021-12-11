import os
import random
import string
import shutil

import nox


@nox.session
def lint(session):
    session.install("flake8", "flake8-import-order")
    session.run("flake8")


@nox.session
def test(session):
    sdist_dir = os.path.join(session.virtualenv.location, "sdist")
    if os.path.exists(sdist_dir):
        shutil.rmtree(sdist_dir, ignore_errors=True)
    session.run("python", "setup.py", "sdist", "--dist-dir", sdist_dir, silent=True,)
    generated_files = os.listdir(sdist_dir)
    assert len(generated_files) == 1
    generated_sdist = os.path.join(sdist_dir, generated_files[0])
    session.install(generated_sdist, "pytest")
    mojeto_config_location = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    print("nox: ", mojeto_config_location)
    print(os.environ)
    os.environ["MOJETO_CONFIG_LOCATION"] = f"/tmp/{mojeto_config_location}"
    session.run("pytest")
