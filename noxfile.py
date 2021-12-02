import nox


@nox.session
def lint(session):
    session.install("flake8", "flake8-import-order")
    session.run("flake8")
