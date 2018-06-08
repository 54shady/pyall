#!/usr/bin/env python
# coding=utf-8

# 先定义一个闭包
def wrapper(func):
    def closure():
        print('Accessable checking...')
        func()

    return closure

# 假设要在每次调用function1前做一个权限检查
# 假设是打印一下Accessable checking
def function1():
    print('calling function1')

# python中的装饰器,在函数外面@装饰器
@wrapper
def function2():
    print('calling function2')

# step 1 使用一个新变量接收闭包里的函数指针(closure)
function_point = wrapper(function1)
function_point()

# step 2, 重新赋值function1
function1 = wrapper(function1)
function1()

# python中的在函数开头加上@装饰器就等同上面step2的语法
print('-'*20)
function2()
