#!/usr/bin/env python
# coding=utf-8

import time

class Person(object):
    '''
    1. 静态方法是类中的函数,不需要实例
    2. 静态方法主要是用来存放逻辑性的代码
        和类本身没有交互,即在静态方法中,不会涉及到类中的方法和属性的操作
    3.  可以在类外面写一个简单的方法来做这些,但是这样做就扩散了类代码的关系到类定义的外面
        这样写就会导致以后代码维护的困难
    '''
    @staticmethod
    def print_time():
        print time.strftime("%H:%M:%S", time.localtime())

    '''
    1. 类方法和静态方法区别在于,不管这个方法是从实例调用还是从类调用,它都用第一个参数把类传递过来
    2 .类方法一般会和类相关属性或内部方法有牵扯
    '''
    # 获取类中的属性
    @classmethod
    def print_personinfo(cls):
        print '%s age %d' % (cls.name, cls.age)

    # 给类添加属性
    @classmethod
    def set_name_age(cls, n, a):
        cls.name = n
        cls.age = a

if __name__ == '__main__':
    # 类方法和静态方法都可以用类直接调用而不需要使用实例调用
    Person.print_time()

    Person.set_name_age('anonymous', 911)
    Person.print_personinfo()
