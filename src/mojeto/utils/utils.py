def prompt_yes_no(question, default="yes"):
    choices = {
        "yes": True,
        "y": True,
        "no": False,
        "n": False
    }
    options = "(Y/n)" if default == "yes" else "(y/N)"

    choice = input(f"{question} {options}: ").lower()
    if choice in choices:
        return choices[choice]
    elif choice == "":
        return choices[default]
    else:
        return choices["no"]
