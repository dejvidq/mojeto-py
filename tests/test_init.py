from mojeto.cli.init import Init
from pathlib import Path


class TestInit:

    def test_init_e2e(self, repo_location):
        assert not Path(repo_location).is_dir()
        assert not Path(f"{repo_location}/.mojeto").is_file()
        init_obj = Init(location=repo_location)
        init_obj()
        assert Path(repo_location).is_dir()
        assert Path(f"{repo_location}/.mojeto").is_file()


