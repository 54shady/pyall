#!/usr/bin/env python
# coding=utf-8

import subprocess

'''其中shell参数为False时,命令需要通过列表的方式传入,当shell为True时,可直接传入命令'''

a = subprocess.call(['df', '-hT'], shell=False)
print('-'*50)
a = subprocess.call('df -hT', shell=True)
