#!/usr/bin/env python
# coding=utf-8

from multiprocessing import Pool
import time
import os

NUMBER=3

def start_routine():
    for i in range(4):
        print('routine...pid(%d)' % os.getpid())
        time.sleep(1)

# 创建一个NUMBER个进程的进程池
po = Pool(NUMBER)

for i in range(10):
    po.apply_async(start_routine)

print('-----start----')
# 关闭进程池
po.close()

# 主进程需要等待进程池里的子进程结束
po.join()
print('-----end----')
