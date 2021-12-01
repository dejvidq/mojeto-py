from argparse import ArgumentParser
from mojeto.cli.init import Init


parser = ArgumentParser(description="Take care of your dotfiles")
exclusive = parser.add_mutually_exclusive_group()
exclusive.add_argument('-b', '--backup', help="Do backup", action='store_true')
exclusive.add_argument('-a', '--apply', help="Apply files", action='store_true')
exclusive.add_argument('-i', '--init', help="Initialize configuration", nargs="*")

args = parser.parse_args()


def main():
    if args.init is not None:
        if len(args.init) > 0:
            init = Init(args.init[0])
        else:
            init = Init()
        init.initialize()
    print("Hello World")
