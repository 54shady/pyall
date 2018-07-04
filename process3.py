#!/usr/bin/env python
# coding=utf-8

# ps aux 查看只要子进程不结束的话主进程也不会结束
# 这点和C里的不同
# 在C语言里主进程不主动等待子进程的话主进程就会结束
from multiprocessing import Process
import time

# 自定义process类
# 1. 继承Process
# 2. 实现run方法
class myProcess(Process):
    # 一定要实现run方法
    def run(self):
        while True:
            print('my process run...')
            time.sleep(1)

p = myProcess()
p.start()

while True:
    print('main process...')
    time.sleep(1)
