#!/usr/bin/env python
# coding=utf-8

import subprocess

'''其中shell参数为False时,命令需要通过列表的方式传入,当shell为True时,可直接传入命令'''

'''将一个子进程的输出,作为另一个子进程的输入'''
child1 = subprocess.Popen(["cat", "/etc/passwd"], stdout=subprocess.PIPE)
child2 = subprocess.Popen(["grep", "0:0"], stdin=child1.stdout,
        stdout=subprocess.PIPE)

out = child2.communicate()
print out
