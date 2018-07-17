#!/usr/bin/env python
# coding=utf-8

#import subcmds # trigger the __init__.py being called
from subcmds import all_commands # trigger the __init__.py being called

cmd_key = ('cmd_foo', 'cmd_bar') # 通过关键字调用子文件夹里的方法

def main():
    for k in cmd_key:
        all_commands[k]()

if __name__ == '__main__':
    main()
