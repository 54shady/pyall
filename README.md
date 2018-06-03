# Python all things

## import module

python中查看import模块的路径

	import sys
	sys.path

需要修改路径的话

	sys.path.append('/your_module_path')

## reload module

使用reload可以重新加载模块

	reload(module_name)

## == and is

- is是比较两个引用是否指向同一个对象(引用比较)
- ==是比较两个对象(内容)和是否相等

例子1

	a = [11, 22, 33]
	b = [11, 22, 33]
	a == b //True
	a is b //False

可以用id查看对象指向的内存地址

	id(a)
	id(b)

## 深浅拷贝

例子1(浅拷贝)

	a = [11, 22, 33]
	b = a	//a,b指向同一个内存地址
	id(a)
	id(b)

例子2(深拷贝)可以用id查看a,c是否指向同一个对象

	import copy
	a = [11, 22, 33]
	c = cop.deepcopy(a)
	id(a)
	id(c)
