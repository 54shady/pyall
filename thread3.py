#!/usr/bin/env python
# coding=utf-8

import threading
import time
import random

# 每个线程执行的顺序不确定
class myThread(threading.Thread):
    def run(self):
        time.sleep(random.random())
        print 'hello python %s' % self.name

if __name__ == '__main__':
    # 创建5个线程
    for i in range(5):
        t = myThread()
        t.start() # 执行类里的run方法
