import os
import random
import shutil
import string

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
    session.run("pytest", "-sv")
