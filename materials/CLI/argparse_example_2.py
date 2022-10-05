import argparse
import logging
import sys


class DebugAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if option_string in self.option_strings:
            logging.root.setLevel(logging.DEBUG)


def validate(args):
    print("Validate", args)


def load(args):
    print("Load", args)


def create_parser():
    prog = sys.argv[0]
    if ".py" in prog:
        prog = "python {}".format(prog)
    else:
        prog = None
    parser = argparse.ArgumentParser(prog = prog,
        description='Parse input data file and load to database')
    parser.add_argument("--debug", action=DebugAction, nargs=0, help=argparse.SUPPRESS)

    subparsers = parser.add_subparsers(metavar="command", required=True)

    parser_validate = subparsers.add_parser("validate", help="Validate JSON file with input data format")
    parser_validate.add_argument("scheme", nargs="+", metavar="JSON_SCHEMA")
    parser_validate.set_defaults(func=validate)

    parser_load = subparsers.add_parser("load", help="Parse input data file and load to database")
    parser_load.add_argument("files", nargs="+", metavar="INPUT_DATA_FILE")
    parser_load.add_argument("-c", "--config", action="store", default="config.json",
                             metavar="CONNECTION_CONFIG",
                             help="Configuration file with database settings")
    parser_load.add_argument("-s", "--schema", action="store", required=True,
                             metavar="JSON_SCHEMA", help="JSON schema of input data")
    parser_load.set_defaults(func = load)

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    if "func" in args: # Check subcommand function argument
        args.func(args)
    else:
        parser.print_help()
    return 0

if __name__ == '__main__':
    main()