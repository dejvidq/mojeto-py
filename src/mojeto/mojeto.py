from argparse import ArgumentParser

from mojeto.cli.add import Add
from mojeto.cli.backup import Backup
from mojeto.cli.init import Init


def main() -> None:
    parser = ArgumentParser(description="Take care of your dotfiles")
    exclusive = parser.add_mutually_exclusive_group()
    exclusive.add_argument('-b', '--backup', help="Do backup", action='store_true')
    exclusive.add_argument('-a', '--add', help="Add file")
    exclusive.add_argument('-i', '--init', help="Initialize configuration", nargs="?", const="")

    args = parser.parse_args()

    if args.init is not None:
        init = Init(location=args.init)
        init()
    elif args.add:
        add = Add()
        add(file_path=args.add)
    elif args.backup:
        backup = Backup()
        backup()
