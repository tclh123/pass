# coding=utf-8

from pas.models.platform import Platform


def populate_argument_parser(parser):
    parser.add_argument('action', choices=['add', 'list', 'rm'])
    parser.add_argument('--name', help="platform's name")
    parser.add_argument('--url', help="platform's url")


def main(args):
    if args.action == 'list':
        ps = Platform.gets()
        if ps:
            for p in ps:
                print p
        else:
            print 'Empty'
    elif args.action == 'add':
        p = Platform.add(args.name, args.url)
        print p
    elif args.action == 'rm':
        if Platform.rm(args.name):
            print args.name, 'removed'
        else:
            print 'remove', args.name, 'failed'
