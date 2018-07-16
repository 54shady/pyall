#!/usr/bin/env python
# coding=utf-8

# import local debug info module
from print_debug_info import pdi

# 带有参数的装饰器
# 在运行时起到不同的功能


def pre_wrapper(pre="defaultValue"):
    def wrapper(func):
        print 'pre = %s' % pre

        def closure():
            # 根据装饰器的参数来选择执行的操作
            if pre == 'python':
                func(pre)
            else:
                func()

        return closure

    return wrapper


@pre_wrapper('hello')
def function():
    pdi()


@pre_wrapper('python')
def function1(val):
    pdi()
    print 'val = %s' % val


print('-' * 30)
function()
function1()
