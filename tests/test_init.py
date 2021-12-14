from pathlib import Path

from mojeto.cli.init import Init


class TestInit:

    def test_init_e2e(self, repo_location):
        assert not Path(repo_location).is_dir()
        assert not Path(f"{repo_location}/.mojeto").is_file()
        init_obj = Init(location=repo_location)
        init_obj()
        assert Path(init_obj.repo_location).is_dir()
        assert Path(init_obj.config_path).is_file()

    def test_init_e2e_default_path(self, repo_location):
        assert not Path(repo_location).is_dir()
        assert not Path(f"{repo_location}/.mojeto").is_file()
        init_obj = Init(location="")
        init_obj()
        assert Path(init_obj.repo_location).is_dir()
        assert Path(init_obj.config_path).is_file()

    def test_init_create_working_directory(self, repo_location):
        assert not Path(repo_location).is_dir()
        init_obj = Init(location=repo_location)
        init_obj.create_working_directory()
        assert Path(init_obj.repo_location).is_dir()

    def test_init_create_config_file(self, repo_location_created):
        assert not Path(f"{repo_location_created}/.mojeto:").is_file()
        init_obj = Init(location=repo_location_created)
        init_obj.create_config_file()
        assert Path(init_obj.config_path).is_file()

    def test_init_create_config_file_working_directory_exist(self, repo_location_created):
        assert Path(repo_location_created).is_dir()
        assert not Path(f"{repo_location_created}/.mojeto").is_file()
        init_obj = Init(location=repo_location_created)
        init_obj()
        assert Path(init_obj.repo_location).is_dir()
        assert Path(init_obj.config_path).is_file()

    def test_init_override_config_file(self, repo_location_created_with_config, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "y")
        assert Path(repo_location_created_with_config).is_dir()
        assert Path(f"{repo_location_created_with_config}/.mojeto").is_file()
        init_obj = Init(location=repo_location_created_with_config)
        init_obj()
        assert Path(init_obj.repo_location).is_dir()
        assert Path(init_obj.config_path).is_file()

