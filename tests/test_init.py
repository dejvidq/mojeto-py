from pathlib import Path

from mojeto.cli.init import Init


class TestInit:

    def test_init_e2e(self, repo_location):
        assert not Path(repo_location).is_dir()
        assert not Path(f"{repo_location}/.mojeto").is_file()
        init_obj = Init(location=repo_location)
        init_obj()
        assert Path(repo_location).is_dir()
        assert Path(f"{repo_location}/.mojeto").is_file()

    def test_init_create_working_directory(self, repo_location):
        assert not Path(repo_location).is_dir()
        init_obj = Init(location=repo_location)
        init_obj.create_working_directory()
        assert Path(repo_location).is_dir()

    def test_init_create_config_file(self, repo_location_created):
        assert not Path(f"{repo_location_created}/.mojeto:").is_file()
        init_obj = Init(location=repo_location_created)
        init_obj.create_config_file()
        assert Path(f"{repo_location_created}/.mojeto").is_file()
