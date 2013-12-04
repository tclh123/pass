# coding=utf-8

import os
import sys
import logging


BASE_PATH = os.path.abspath(os.path.dirname(__file__))


def main():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    subparsers = parser.add_subparsers(title="commands",
                                       dest="subparser_command")
    subcommands = [
        ('status', 'status', "Show system status"),
        ('st', 'status', "Alias of status"),
        ('platform', 'platform', "Pass platform management"),
        ('pl', 'platform', "Alias of platform"),
        ('account', 'account', "Pass account management"),
        ('ac', 'account', "Alias of account"),
    ]

    for command, module_name, help_text in subcommands:
        try:
            module = __import__('pas.commands.' + module_name,
                                globals(), locals(),
                                ['populate_argument_parser', 'main'])
        except ImportError:
            import traceback
            traceback.print_exc()
            print >>sys.stderr, "Can not import command %s, skip it" % command
            continue

        subparser = subparsers.add_parser(command, description=help_text)
        subparser.add_argument('-v', '--verbose', action='store_true',
                               help="enable additional output")

        module.populate_argument_parser(subparser)
        subparser.set_defaults(func=module.main)

    argv = sys.argv[1:] or ['--help']
    args = parser.parse_args(argv)

    loglevel = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=loglevel)

    return args.func(args)


if __name__ == '__main__':
    main()
