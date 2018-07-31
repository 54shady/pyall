#!/usr/bin/env python
# coding=utf-8


class Person(object):
    def __init__(self, newName, newAge):
        self.name = newName
        self.age = newAge

    def eat(self):
        print '%s is eatting' % self.name

    # 给类添加方法
    # 静态方法
    @staticmethod
    def fly():
        print 'staticmethod, fly'

    # 类方法, 和静态方法区别在于第一个参数永远都是类对象
    @classmethod
    def read(cls):
        print 'classmethod, read'


if __name__ == '__main__':
    # 使用类的静态方法和类方法都不需要实例
    Person.fly()
    Person.read()
