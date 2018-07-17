#!/usr/bin/env python
# coding=utf-8

import os

print 'this is __init__.py being calling'
cwd = os.path.dirname(__file__)

all_commands = {}

# 加载所有子文件夹里的py文件
# 并导入模块中的方法
for py in os.listdir(cwd):
    if py == '__init__.py': # 过滤掉本文件
        continue

    if py.endswith('.py'): # 加载所有py文件
        name = py[:-3]

        # 导入所有py文件里的方法
        mod = __import__(__name__,
                globals(),
                locals(),
                ['%s' % name])

        mod = getattr(mod, name)
        cmd_name = 'cmd_' + name

        try:
            cmd = getattr(mod, cmd_name)
        except AttributeError:
            raise SyntaxError('%s/%s does not define class %s' % (
                                            __name__, py, cmd_name))

        # 添加到全局字典中
        all_commands[cmd_name] = cmd
