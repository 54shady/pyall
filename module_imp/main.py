#!/usr/bin/env python
# coding=utf-8

import imp
import sys

def main():
    # find say_hello.py
    info = imp.find_module('say_hello', ['./localmodule/'])
    print info

    # load_module第一个参数是module的别名
    # import say_hello as SayHello
    mod = imp.load_module("SayHello", *info)
    print dir(mod)

    print '=' * 30

    # find say_goodbye.py
    f, fn, desc = imp.find_module('say_goodbye', ['./localmodule/'])
    print f, fn, desc

    # import say_goodbye as say_goodbye
    mod = imp.load_module("say_goodbye", f, fn, desc)
    print dir(mod)

if __name__ == '__main__':
    main()
