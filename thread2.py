#!/usr/bin/env python
# coding=utf-8

import threading
import time

# 自定义thread类
# 和线程一样
# 需要继承基类(threading.Thread)
# 实现run方法即可
class myThread(threading.Thread):
    def run(self):
        print 'hello python %s' % self.name
        time.sleep(1)

if __name__ == '__main__':
    # 创建5个线程
    for i in range(5):
        t = myThread()
        t.start() # 执行类里的run方法
