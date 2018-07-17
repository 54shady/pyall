#!/usr/bin/env python
# coding=utf-8

""" python builtin function 'super' usage
super函数是用于调用父类(超类)的一个方法
super是用来解决多重继承问题的
直接用类名调用父类方法在使用单继承的时候没问题
但是如果使用多继承,会涉及到查找顺序(MRO),重复调用(钻石继承)等种种问题
"""


class Parent(object):
    def __init__(self):
        print 'parent init'

    def foo(self):
        print 'parent foo'


class Child(Parent):
    def __init__(self):
        """ call parent init before local """
        super(Child, self).__init__()
        print 'child init'

    def foo(self):
        """ call parent foo before local """
        super(Child, self).foo()
        print 'child foo'

    def bar(self):
        """ call parent bar before local """
        super(Child, self).foo()
        print 'child bar'


def main():
    c = Child()
    print '-' * 30
    c.foo()
    print '-' * 30
    c.bar()


if __name__ == '__main__':
    main()
