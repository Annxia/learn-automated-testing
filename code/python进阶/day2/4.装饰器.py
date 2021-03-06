# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: 4.装饰器.py
# @ide: PyCharm
# @time: 2020/6/30 15:41
print("")
'''
装饰器本质上是一个函数，该函数用来处理其他函数，它可以让其他函数在不需要修改
代码的前提下增加额外功能，装饰器的返回值也是一个函数对象。它经常用于有切面需
求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等应用场景。
装饰器可以抽离出大量与函数功能本身无关的雷同代码并继续重用。

'''

# 开放封闭原则：允许扩展已有功能代码，但是不允许修改已有代码
def bar(f):
    """
    函数接受一个参数
    函数里边定义一个内部函数
    将定义的内部函数作为返回值返回
    :param f:接受的参数就是被装饰函数，也就是需要增加新功能的函数
    :return:装饰完成后的函数
    """
    def inner():
        f() # 需要保留被装饰函数原有的功能，所以通过参数传递的方式调用被装饰函数
        print("加上了新功能")

    return inner

@bar  #这个操作就相当于 foo = bar(foo)
def foo():
    print("成功实现了一系列功能")


# foo = bar(foo) # 将inner赋值给foo
foo() # 调用foo,就相当于调用inner