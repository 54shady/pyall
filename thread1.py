#!/usr/bin/env python
# coding=utf-8

import threading
import time

def start_routine():
    print 'hello python thread'
    time.sleep(1)

if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=start_routine)
        t.start()
