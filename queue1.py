#!/usr/bin/env python
# coding=utf-8

from multiprocessing import Process, Queue
import time
import random

# 使用队列来实现进程间通信

# 不断向队列中写消息


def write(q):
    for value in ['A', 'B', 'C']:
        print 'put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())

# 不断读取队列中消息,直到队列中无消息


def read(q):
    while True:
        if not q.empty():
            v = q.get(True)  # 等价于q.get_nowait()非阻塞
            print 'get %s from queue' % v
            time.sleep(random.random())
        else:
            break


if __name__ == '__main__':
    # 父进程创建消息队列,并传给子进程
    q = Queue()  # 该消队列无限大
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    # 启动子进程写消息
    pw.start()

    # 等待写进程结束
    pw.join()

    # 启动读进程读消息
    pr.start()

    # 等待读进程读完所有消息
    pr.join()
