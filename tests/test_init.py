from pathlib import Path, PurePath

from mojeto.cli.init import Init
from mojeto.constants import CONFIG_PATH


class TestInit:

    def test_init_create_working_directory(self, repo_name):
        init_obj = Init(location=repo_name)
        init_obj.create_working_directory()
        assert Path(repo_name).is_dir()

    def test_init_create_config_file(self, generate_repo):
        repo_location = generate_repo
        config_file = Path(f"{repo_location}/.mojeto")
        mojeto_init_obj = Init(location=repo_location)
        mojeto_init_obj.create_config_file(config_path=config_file)
        assert config_file.is_file()

    # def test_init_create_config_file_override(self, generate_repo_with_config):
        # repo_location = generate_repo_with_config
        # config_file = Path(f"{repo_location}/.mojeto")
        # mojeto_init_obj = Init(location=repo_location)
        # mojeto_init_obj.create_config_file(config_path=config_file, override=True)
        # assert config_file.is_file()

    def test_init_create_config_file_folder_exist(self, generate_repo_without_config):
        repo_location = Path(generate_repo_without_config)
        assert repo_location.is_dir()
        assert not Path(PurePath(repo_location, ".mojeto")).is_file()
        mojeto_init_obj = Init(location=repo_location)
        mojeto_init_obj()
        assert Path(PurePath(repo_location, ".mojeto")).is_file()

    def test_init_folder_and_config_exist(self, monkeypatch, generate_repo_with_config):
        monkeypatch.setattr('builtins.input', lambda _: "y")
        repo_location = generate_repo_with_config
        mojeto_init_obj = Init(location=repo_location)
        mojeto_init_obj()
        assert Path(repo_location).is_dir()
        assert Path(PurePath(repo_location, ".mojeto")).is_file()

    def test_init_folder_and_config_do_not_exist(self):
        repo_location = Path(CONFIG_PATH).parents[0]
        assert not Path(repo_location).is_dir()
        mojeto_init_obj = Init(location=repo_location)
        mojeto_init_obj()
        assert Path(repo_location).is_dir()
        
