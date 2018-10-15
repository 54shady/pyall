#!/usr/bin/env python
# coding=utf-8

"""
time python thread6.py
由于加锁位置的不一样
会导致执行的效率不一样
"""

import threading

# 线程共享全局变量
g_cnt = 0


def start_routine_a(lock):
    global g_cnt

    # 尝试获取锁,如果未获取到锁则阻塞
    lock.acquire()
    for i in range(10000000):
        g_cnt += 1
    lock.release()
    print 'g_cnt = %d' % g_cnt


def start_routine_b(lock):
    global g_cnt

    # 尝试获取锁,如果未获取到锁则阻塞
    lock.acquire()
    for i in range(10000000):
        g_cnt += 1
    lock.release()
    print 'g_cnt = %d' % g_cnt


if __name__ == '__main__':
    print 'global cnt = %d' % g_cnt

    # 创建互斥锁
    mutex = threading.Lock()

    t1 = threading.Thread(target=start_routine_a, args=(mutex,))
    t2 = threading.Thread(target=start_routine_b, args=(mutex,))
    t1.start()
    t2.start()
