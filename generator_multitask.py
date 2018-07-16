#!/usr/bin/env python
# coding=utf-8

# 三种形式多任务: 进程,线程,协程
# 本例即为协程

# 只要task1和task2切换足够快
# 就相当于有两个任务同时运行


def task1():
    while True:
        print('task one running---')
        yield None


def task2():
    while True:
        print('task two running+++')
        yield None


t1 = task1()
t2 = task2()

# main loop
while True:
    # __next__ python3 feature
    next(t1)  # t1.__next__()
    next(t2)  # t2.__next__()
