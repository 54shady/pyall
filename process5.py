#!/usr/bin/env python
# coding=utf-8

from multiprocessing import Pool
import time
import os

NUMBER = 3


def start_routine(index):
    for i in range(4):
        print('routine loop[%d] pid(%d), task(%d)' % (i, os.getpid(), index))
        time.sleep(1)


# 创建一个NUMBER个进程的进程池
po = Pool(NUMBER)

for i in range(10):
    print 'push task %d to Pool' % i
    # 使用元组的方式给子进程传参数
    po.apply_async(start_routine, (i,))

print('stop push task to poll...')
# 关闭进程池
po.close()

# 主进程需要等待进程池里的子进程结束
po.join()
print('-----end----')
