from pathlib import Path

import yaml

from mojeto.constants import CONFIG_PATH


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


def update_path_in_config(new_path: str):
    with open(CONFIG_PATH, 'r') as f:
        config_content = yaml.safe_load(f.read())
    config_content[0]['files_location']['path'] = new_path
    with open(CONFIG_PATH, 'w') as f:
        yaml.dump(config_content, f)
