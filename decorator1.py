#!/usr/bin/env python
# coding=utf-8

"""
装饰器应用实例
装饰器装饰顺序,从上往下对应从外到内
装饰器实质就是调用了闭包函数wrapper
"""


def makeBold(fn):
    def wrapper():
        return "<b>" + fn() + "</b>"

    return wrapper


def makeItalic(fn):
    def wrapper():
        return "<i>" + fn() + "</i>"

    return wrapper


@makeBold
def title_one():
    return "hello decorator"


@makeItalic
def title_two():
    return "hello decorator"


@makeBold
@makeItalic
def title_three():
    return "hello decorator"


@makeItalic
@makeBold
def title_four():
    return "hello decorator"


boldTitle = title_one()
print(boldTitle)

italicTitle = title_two()
print(italicTitle)

boldItalicTitle = title_three()
print(boldItalicTitle)

italicBoldTitle = title_four()
print(italicBoldTitle)
