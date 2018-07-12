#!/usr/bin/env python
# coding=utf-8

def sayHello(info):
    print 'say hello.....'

def sayHelloTo(*info):
    #print dir(info)
    print 'say hello to %s' % info[1]
