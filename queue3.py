#!/usr/bin/env python
# coding=utf-8

from multiprocessing import Manager, Pool
import os, time, random

# 进程池中的进程间使用队列通信

# 不断向队列中写消息
def write(q):
    for value in "queue_msg":
        print '==> %s' % value
        q.put(value)

# 不断读取队列中消息,直到队列中无消息
def read(q):
    while not q.empty():
        v = q.get(True) # 等价于q.get_nowait()非阻塞
        print '<== %s' % v

if __name__ == '__main__':
    # 父进程创建消息队列,并传给子进程
    # 这里要使用给进程池专用的queue
    q = Manager().Queue()
    po = Pool()

    # 使用阻塞方式
    # 先写消息后读
    po.apply(write, (q,))
    po.apply(read, (q,))

    # 停止向进程池中进程添加任务
    po.close()
    po.join()
