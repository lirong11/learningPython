#!/usr/bin/python

class MyClass:
    """一个简单的类实例"""
    i = 12345
    def f(self):
        return 'hello world'

#类实例化
x = MyClass()

#访问类的属性和方法
print("MyClass类的属性i为：",x.i)
print('MyClass类的方法f输出为：',x.f())

#类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用
class Complex:
    def __init__(self,realpart,imagpart):
        self.r = realpart
        self.i = imagpart

y = Complex(3.0,-4.5)
print(y.r,y.i)

#self代表类的实例，而非类,类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self
class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()

#self不是python的关键字，我们可以把他换成其他也是可以正常运行
class Leerong:
    def prt(leerong):
        print(leerong)
        print(leerong.__class__)

l = Leerong()
l.prt()