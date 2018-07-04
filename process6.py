#!/usr/bin/env python
# coding=utf-8

from multiprocessing import Pool
import time
import os

NUMBER=3

def start_routine(index1, index2):
    for i in range(4):
        print('pid(%d), index1(%d) index2(%d)' % (os.getpid(), index1, index2))
        time.sleep(1)

# 创建一个NUMBER个进程的进程池
po = Pool(NUMBER)

for i in range(10):
    # 使用元组的方式给子进程传参数
    po.apply_async(start_routine, (i, i+2))

print('-----start----')
# 关闭进程池,此时不能在往进程池里添加任务
po.close()

# 主进程需要等待进程池里的子进程结束
# 没有调用join的话会导致进程中任务无法正确执行
po.join()
print('-----end----')
