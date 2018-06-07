#!/usr/bin/env python
# coding=utf-8

import subprocess

'''其中shell参数为False时,命令需要通过列表的方式传入,当shell为True时,可直接传入命令'''

'''在当前目录下创建一个suprocesstest的目录'''
a = subprocess.Popen('mkdir subprocesstest', shell=True, cwd='.')
