#!/usr/bin/env python
# coding=utf-8

import argparse


def main():
    """
        Usage
        :!python % -v 2 -a 3 -c -d sdf 23 -e -b
        :!python % -v 2 -a 3 -c -d sdf 23
    """
    parser = argparse.ArgumentParser(description="Demo of argparse module")

    # 第一种 : 带参数变量(比较常用)
    # -v <number>
    parser.add_argument("-v", "--verbosity", type=int,
                        help="increase output verbosity")

    # -a 1, -a 2, -a 3
    parser.add_argument("-a", "--arange", type=int,
                        help="input the range value", choices=[1, 2, 3])

    # -c, -cc, -ccc(用处比较少)
    parser.add_argument(
        "-c", "--cnt", help="count action demo", action="count")

    # dnt 默认值是3, -d ==> 默认是4 (用处比较少)
    parser.add_argument(
        "-d", "--dnt", help="count action with default value", action="count", default=3)

    # 第二种 : Optional arguments : 可选参数,bool变量(比较常用)
    parser.add_argument(
        "-b", "--bbb", help="this is a enable value b", action="store_true")
    parser.add_argument(
        "-e", "--eee", help="this is a enable value e", action="store_false")

    # 第三种 : Positional arguments : 固定参数(使用的场景相对较少)
    parser.add_argument("pvalue", help="this is an positional value")
    parser.add_argument("pvalue_int", help="positional type int", type=int)

    args = parser.parse_args()

    print 'verbosity is %s' % args.verbosity

    if args.bbb:
        print 'enable'
    else:
        print 'disable'

    if args.eee:
        print 'enable'
    else:
        print 'disable'

    print 'positional value is %s' % args.pvalue
    print 'positional value_int is %d' % args.pvalue_int

    print 'arange value is %d' % args.arange
    print 'cnt value is %d' % args.cnt
    print 'dnt value is %d' % args.dnt


if __name__ == '__main__':
    main()
