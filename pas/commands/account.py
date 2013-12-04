# coding=utf-8

from pas.models.account import Account


def populate_argument_parser(parser):
    parser.add_argument('action', choices=['add', 'list', 'rm'])
    parser.add_argument('-u', '--uid', help="account's uid")
    parser.add_argument('-p', '--passwd', help="account's passwd")
    parser.add_argument('-P', '--platform', help="account's platform")
    parser.add_argument('-n', '--name', help="account's name")
    parser.add_argument('-e', '--email', help="account's email")
    parser.add_argument('--phone', help="account's phone")


def main(args):
    if args.action == 'list':
        accs = Account.gets()
        if accs:
            for a in accs:
                print a
        else:
            print 'Empty'
    elif args.action == 'add':
        a = Account.add(args.uid, args.passwd, args.platform,
                        args.name, args.email, args.phone)
        print a
    elif args.action == 'rm':
        if Account.rm(args.uid, args.platform):
            print args.uid, 'of', args.platform, 'removed'
        else:
            print 'remove', args.uid, 'of', args.platform, 'failed'
