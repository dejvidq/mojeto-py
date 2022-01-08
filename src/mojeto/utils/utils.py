from pathlib import Path


def prompt_yes_no(question, default="yes"):
    choices = {
        "yes": True,
        "y": True,
        "no": False,
        "n": False
    }
    options = "(Y/n)" if default in ["yes", "y"] else "(y/N)"

    choice = input(f"{question} {options}: ").lower()
    if choice in choices:
        return choices[choice]
    elif choice == "":
        return choices[default]
    else:
        return choices["no"]


def encode_file_path(src_path: Path):
    path = src_path.parent
    home = Path.home()
    if home in src_path.parents:
        path = Path(src_path.parents[0].as_posix().replace(home.as_posix(), "%HOME%", 1))
    return path.as_posix()


def decode_file_path(path: str):
    return path.replace("%HOME%", Path.home().as_posix())
