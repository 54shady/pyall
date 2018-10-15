#!/usr/bin/env python
# coding=utf-8

import threading
import time

# 线程共享全局变量
g_cnt = 100


def start_routine_a():
    global g_cnt
    g_cnt = 1024
    print 'routine a %d' % g_cnt


def start_routine_b():
    global g_cnt
    print 'routine b %d' % g_cnt


def start_routine_c(arg):
    arg.append(4)
    print arg


def start_routine_d(arg):
    print arg


if __name__ == '__main__':
    g_list = [1, 2, 3]
    print 'global cnt = %d' % g_cnt
    t1 = threading.Thread(target=start_routine_a)
    t2 = threading.Thread(target=start_routine_b)
    t1.start()
    time.sleep(1)
    t2.start()

    t3 = threading.Thread(target=start_routine_c, args=(g_list,))
    t4 = threading.Thread(target=start_routine_d, args=(g_list,))
    t3.start()
    time.sleep(1)
    t4.start()
