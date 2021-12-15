import pytest

from mojeto.cli.add import Add
from mojeto.config import Config


class TestAdd:

    @pytest.mark.usefixtures("init")
    def test_add(self, tmp_file):
        config = Config()
        assert not config.get_all_files()
        add = Add()
        add(tmp_file)
        config = Config()
        assert len(config.get_all_files()) == 1

    @pytest.mark.usefixtures("init")
    def test_add_same_file_multiple_times(self, tmp_file):
        config = Config()
        assert not config.get_all_files()
        add = Add()
        add(tmp_file)
        add(tmp_file)
        config = Config()
        assert len(config.get_all_files()) == 1
