#!/usr/bin/env python
# coding=utf-8


class ContextManagerDemo():
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print 'Enter >>>'
        return self

    def __exit__(self, *args):
    #def __exit__(self, exc_type, exc_value, traceback):
        print '<<< Exit'
        del self

    def print_info(self):
        print 'This is %s' % self.name


def main():
    f = open('context_manager.py', 'r')
    print f.closed  # whether the file is closed ?
    f.close()
    print f.closed

    with open('context_manager.py', 'r') as f:
        print f.closed  # process the file
    print f.closed  # close the file automatic

    # 自定义上下文管理
    with ContextManagerDemo("demo_aaa") as cm:
        cm.print_info()


    cm2 = ContextManagerDemo("demo_bbb")
    try:
        cm2.__enter__()
        cm2.print_info()
    finally:
        cm2.__exit__()

if __name__ == '__main__':
    main()
