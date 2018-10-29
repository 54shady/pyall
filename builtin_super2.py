#!/usr/bin/env python
# coding=utf-8

"""
有如下钻石继承

          Base
        /     \
    Medium1     Medium2
        \      /
          Leaf
如果在子类中还是用普通方法访问父类
就会导致父类多次调用
"""

""" 普通方法操作 """


class Base():
    def __init__(self):
        print 'Base init'


class Medium1(Base):
    def __init__(self):
        Base.__init__(self)
        print 'Medium1 init'


class Medium2(Base):
    def __init__(self):
        Base.__init__(self)
        print 'Medium2 init'


class Leaf(Medium1, Medium2):
    def __init__(self):
        Medium1.__init__(self)
        Medium2.__init__(self)
        print 'Leaf init'


leaf = Leaf()
print '-' * 40

""" 使用super操作 """


class BaseSuper(object):
    def __init__(self):
        self.name = "base"
        print '%s init' % self.name

    def give_u_my_name(self):
        return self.name


class Medium1Super(BaseSuper):
    def __init__(self):
        super(Medium1Super, self).__init__()
        print 'Medium1 init'


class Medium2Super(BaseSuper):
    def __init__(self):
        super(Medium2Super, self).__init__()
        print 'Medium2 init'


class LeafSuper(Medium1Super, Medium2Super):
    def __init__(self):
        super(LeafSuper, self).__init__()
        print 'Leaf init'

    def ask_u_name(self):
        name = super(LeafSuper, self).give_u_my_name()
        print 'haha, u name is %s' % name


leafsuper = LeafSuper()
leafsuper.ask_u_name()
