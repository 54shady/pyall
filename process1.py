#!/usr/bin/env python
# coding=utf-8

# ps aux 查看只要子进程不结束的话主进程也不会结束
# 这点和C里的不同
# 在C语言里主进程不主动等待子进程的话主进程就会结束
from multiprocessing import Process
import time


def start_routine():
    while True:
        print('routine...')
        time.sleep(1)


p = Process(target=start_routine)
p.start()
