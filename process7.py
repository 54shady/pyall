#!/usr/bin/env python
# coding=utf-8

# ps aux 查看只要子进程不结束的话主进程也不会结束
# 这点和C里的不同
# 在C语言里主进程不主动等待子进程的话主进程就会结束
from multiprocessing import Process
import time

NUMBER = 5


def start_routine(name, index):
    while True:
        print 'name = %s, index = %d' % (name, index)
        time.sleep(1)


# 传给子进程的参数写在args的元组里
# 最后一个要留空
p = Process(target=start_routine, args=("debug", 999, ))
p.start()

# 主进程阻塞在这里等待子进程(NUMBER秒)结束后才继续往下走
# p.join() 不传参数表示永远等待
p.join(NUMBER)
print('main...')
