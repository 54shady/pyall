#!/usr/bin/env python
# coding=utf-8

from ctypes import cdll, pydll, PyDLL, CDLL,\
    c_char, byref, create_string_buffer,\
    c_int, c_char_p, Structure, pointer,\
    sizeof, CFUNCTYPE

testlib = CDLL('./testlib.so')

testlib.vv_func()
print 'value = %d' % testlib.get_value()
print '-' * 30

# 这里设置和不设置参数类型差异不明显
testlib.set_value.argtypes = [c_int]
testlib.set_value(911)
print 'value = %d' % testlib.get_value()

testlib.set_value(c_int(811))
print 'value = %d' % testlib.get_value()

# 需要设置函数返回值
testlib.get_string.restype = c_char_p
testlib.get_string()
print 'cstring = %s' % testlib.get_string()

# 这里设置和不设置参数类型差异不明显
testlib.set_string.argtypes = [c_char_p]
testlib.set_string("Pystring")
print 'cstring = %s' % testlib.get_string()

# 这里不设置参数能够很明显看出差异
testlib.set_string2.argtypes = [c_char_p, c_char]
testlib.set_string2("yystring", "P")
print 'cstring = %s' % testlib.get_string()

# 不显示设置参数类型的话需要显示传递
testlib.set_string2(c_char_p("yystring"), c_char('P'))
print 'cstring = %s' % testlib.get_string()

print '-' * 10 + ' byref ' + '-' * 10
# 需要 C 函数修改传入的参数
# 需要按引用传递
val = c_int()
testlib.get_value2(byref(val))
print 'value = %d' % val.value

s = create_string_buffer(10)
testlib.get_string2(byref(s))
print 'cstring = %s' % s.value
testlib.get_string2(s)
print 'cstring = %s' % s.value

print '-' * 10 + ' Struct ' + '-' * 10
'''
struct Point {
    int x;
    int y;
};

struct Rect {
    struct Point upperleft;
    struct Point lowerright;
};
'''
class Point(Structure):
    _fields_ = [
        ('x', c_int),
        ('y', c_int)
    ]

point1 = Point(y = 2)
print 'x = %d, y = %d' % (point1.x, point1.y)

point2 = Point(5, 10)
print 'x = %d, y = %d' % (point2.x, point2.y)

class Rect(Structure):
    _fields_ = [
        ('upperleft', Point),
        ('lowerright', Point)
    ]

rect = Rect(point1, point2)
print '%d %d %d %d' % (rect.upperleft.x,
                        rect.upperleft.y,
                        rect.lowerright.x,
                        rect.lowerright.y)

# 参数是结构体, 指针变量, 引用
point3 = Point()
testlib.set_struct(point1, pointer(point2), byref(point3))
print 'Point3(%d, %d)' % (point3.x, point3.y)

print '-' * 10 + ' Array ' + '-' * 10
TenIntArray = c_int * 5
arr1 = TenIntArray() # int arr1[5]
for i in arr1:
    print i

print '-' * 30
arr2 = TenIntArray(1, 3, 4, 88, 91)
for i in arr2:
    print i

print '-' * 10 + ' Pointer ' + '-' * 10
i = c_int(911) # int i
pi = pointer(i) # int *pi = &i
print '*pi = %d' % pi[0] # *pi 指针解引用使用 [0]

print '-' * 10 + ' Parameter ' + '-' * 10
libc1 = cdll.LoadLibrary('libc.so.6')
libc2 = pydll.LoadLibrary('libc.so.6')
libc3 = CDLL('libc.so.6')
libc4 = PyDLL('libc.so.6')
'''
ctypes允许你创建自定义参数类型
它会自动去搜索自定义数据的_as_parameter_属性
将其作为 C 函数的参数
'''
class Bottles(object):
    def __init__(self, number):
        self._as_parameter_ = number  # here only accept integer, string, unicode string

bottles = Bottles(911)
libc1.printf('%d bottles of beer\n', bottles)
libc2.printf('%d bottles of beer\n', bottles)
libc3.printf('%d bottles of beer\n', bottles)
libc4.printf('%d bottles of beer\n', bottles)


print '-' * 10 + ' String ' + '-' * 10
'''
Python默认的string是不可变的
所以不能传递string到一个C函数去改变它的内容
所以需要使用create_string_buffer
对应 Unicode字符串,要使用create_unicode_buffer
'''
s1 = create_string_buffer(20)
print sizeof(s1)
print repr(s1.raw)
s1.raw = 'hello ctypes'
print repr(s1.raw)
print s1.value

print '-' * 10 + ' NULL ' + '-' * 10
p = c_char_p()
testlib.null_func(p)

print '-' * 10 + ' CallBackFunction ' + '-' * 10
# C 中回调函数的原型为int (*call_back)(int)
# 则在python中也定义一个这也的函数
def python_handler(a):
    print 'python callback being called...'
    return a + 911;

# 使用CFUNCTYPE描述回调函数
# CFUNCTYPE(restype, *argtypes, **kw)
callback_wrap = CFUNCTYPE(c_int, c_int)

# 使用callback_wrap来修饰python中的函数再传递到C
c_handler = callback_wrap(python_handler)
ret = testlib.test_callback(c_int(89), c_handler)
print 'ret = %d' % ret
