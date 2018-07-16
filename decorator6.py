#!/usr/bin/env python
# coding=utf-8

# import local debug info module
from print_debug_info import pdi

# 通用的装饰器
# 处理返回值和不定参数


def wrapper(func):
    def closure(*args, **kwargs):
        r = func(*args, **kwargs)
        return r

    return closure


@wrapper
def function():
    return "calling function done"


@wrapper
def function1():
    pdi()


@wrapper
def function2(a):
    print 'val = %d' % a


@wrapper
def function3(a, b):
    print 'val1 = %d, val2 = %d' % (a, b)
    return "yes"


# 因为装饰后function实质已经指向了闭包closure
ret = function()
print 'ret = %s' % ret

ret = function1()
print 'ret = %s' % ret

ret = function2(911)
print 'ret = %s' % ret

ret = function3(1, 3)
print 'ret = %s' % ret
