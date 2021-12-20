import os

from mojeto.cli.backup import Backup


class TestBackup:

    def test_backup(self, init_with_file):
        _, file = init_with_file
        content_before = self.read_file_content(file)
        self.override_file_content(file)
        backup = Backup()
        backup()
        content_after = self.read_file_content(file)
        assert not content_before == content_after

    def test_backup_file_does_not_exist(self, init_with_file, capfd):
        _, file = init_with_file
        self.remove_file(file)
        backup = Backup()
        backup()
        out, _ = capfd.readouterr()
        assert out.strip() == f"File {file} does not exist. Omitting"

    def read_file_content(self, file):
        with open(file, "r") as f:
            return f.read()

    def override_file_content(self, file):
        with open(file, "w+") as f:
            f.write("AFTER")

    def remove_file(self, filename):
        os.remove(filename)
