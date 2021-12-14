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

    def read_file_content(self, file):
        with open(file, "r") as f:
            return f.read()

    def override_file_content(self, file):
        with open(file, "w+") as f:
            f.write("AFTER")
