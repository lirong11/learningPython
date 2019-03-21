#!/usr/bin/python

#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性，私有属性在类外部无法直接访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print('%s说：我%d岁。'%(self.name,self.age))

#实例化类
p = people('leerong',18,50)
p.speak()


#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构造函数
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print('%s说：我%d岁,我在读%d年级' % (self.name, self.age,self.grade))

s = student('leerong',10,50,5)
s.speak()

class speaker:
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print('我叫%s，我是一个演说家，我演讲的主题是%s'%(self.name,self.topic))

#多重继承
class sample(speaker,student):
    a = ''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

test = sample("Tim",25,80,4,'python')
test.speak()#方法名同，默认调用的是在括号中排前地父类的方法

#定义父类
class Parent:
    def myMethod(self):
        print('调用父类方法')

#定义子类
class Child(Parent):
    def myMethod(self):
        print('调用子类方法')

c = Child()#子类实例
c.myMethod()#子类调用重写方法
super(Child,c).myMethod()#用子类对象调用父类已被覆盖的方法

#类的私有方法
class JustCounter:
    __secretCount = 0#私有变量
    publicCount = 0#公开变量
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
#print(counter.__secretCount)#报错，实例不能访问私有变量

#类的私有方法
class Site:
    def __init__(self,name,url):
        self.name = name #public
        self.__url = url #private

    def who(self):
        print('name：',self.name)
        print('url：',self.__url)

    def __foo(self): #私有方法
        print('这是私有方法')

    def foo(self): #共有方法
        print('这是公共方法')
        self.__foo()

x = Site("百度",'www.baidu.com')
x.who()
x.foo()
#x.__foo()#报错

class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'Vector(%d,%d)'%(self.a,self.b)
    def __add__(self, other):
        return Vector(self.a+other.a,self.b+other.b)

v1 = Vector(2,10)
print(v1)
v2 = Vector(5,-2)
print(v2)
print(v1+v2)