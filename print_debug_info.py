#!/usr/bin/env python
# coding=utf-8

#-*- coding: utf-8 -*-
import inspect

def pdi():
    callerframerecord = inspect.stack()[1]
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)
    print '%s(%s:%d)' % (info.filename, info.function, info.lineno)
