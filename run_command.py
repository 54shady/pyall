#!/usr/bin/env python
# coding=utf-8

import subprocess

# 定义一个用于描述选项的类
class Options():
    def __init__(self):
        self.verbose = False

def run_command(args, **kwargs):
    """Create and return a subprocess.Popen object, printing the command
    line on the terminal if -v was specified."""
    if OPTIONS.verbose:
        print "  running: ", " ".join(args)

    return subprocess.Popen(args, **kwargs)

def main():
    cmd = ['ls', '-la']
    p = run_command(cmd)
    # cmd执行结果输出到子进程的pipe里
    # p = run_command(cmd, stdout = subprocess.PIPE)
    # p.communicate()

if __name__ == '__main__':
    # 全局的OPTIONS
    OPTIONS = Options()
    #OPTIONS.verbose = True # debug command
    main()
