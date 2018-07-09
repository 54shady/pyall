#!/usr/bin/env python
# coding=utf-8

# format concatenate string
def myStringCat(value):
    v = 'value = %d'
    v %= value # concatenate value to the original string
    return v

# not that elegant version
def myStringCatV1(value):
    v = 'value = '
    v += str(value)
    return v

# format long concatenato version
def StringCateL(x, y, z):
    value_template = ("%d %d %d")
    real_value = value_template % (x, y, z)
    return real_value

if __name__ == '__main__':
    print 'input 1 number'
    v = input()
    r1 = myStringCat(int(v))
    r2 = myStringCatV1(v)
    print r1
    print r2

    print 'input 3 number'
    a = input()
    b = input()
    c = input()
    r3 = StringCateL(a, b, c)
    print r3
