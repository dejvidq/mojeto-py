import pytest

from src.mojeto.utils.utils import prompt_yes_no


class TestUtils:

    @pytest.mark.parametrize("answer, exp_result", [("yes", True), ("no", False), ("y", True), ("n", False),
                                                    ("YeS", True), ("nO", False), ("Random", False)])
    def test_prompt_yes_no(self, monkeypatch, answer, exp_result):
        monkeypatch.setattr('builtins.input', lambda _: answer)
        result = prompt_yes_no("Test Question")
        assert result is exp_result

    @pytest.mark.parametrize("default, exp_result", [("yes", True), ("no", False)])
    def test_prompt_yes_no_empty_answer_different_defaults(self, monkeypatch, default, exp_result):
        monkeypatch.setattr('builtins.input', lambda _: "")
        result = prompt_yes_no("Test Question", default=default)
        assert result is exp_result
