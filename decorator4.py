#!/usr/bin/env python
# coding=utf-8


def wrapper(func):
    # 装饰可变长度参数
    def closure(*args, **kwargs):
        return 911 + func(*args, **kwargs)

    return closure


@wrapper
def function(x, y):
    return x + y


@wrapper
def function1(x, y, z):
    return x + y*z


@wrapper
def function2():
    return 0


# 因为装饰后function实质已经指向了闭包closure
# 所以要装饰带参数的函数,闭包函数要和被装饰的参数有相同的形参
ret = function(1, 2)
print 'ret = %d' % ret

ret = function1(1, 2, 3)
print 'ret = %d' % ret

ret = function2()
print 'ret = %d' % ret
