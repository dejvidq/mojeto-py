def prompt_yes_no(default="yes"):
    choices = {
        "yes": True,
        "y": True,
        "no": False,
        "n": False
    }

    choice = input().lower()
    if choice in choices:
        return choices[choice]
    elif choice == "":
        return choices[default]
    else:
        return choices["no"]
