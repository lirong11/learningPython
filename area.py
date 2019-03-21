#!/usr/bin/python3


#计算面积
def area(width,height):
    return width*height


def welcome(name):
    return "welcome", name


a, b = welcome("leerong")
print(a, b)

w = 4
h = 5
print("width = ", w, "height = ", h, "area = ", area(w, h))


'''
    定义一个函数：给函数一个民称，指定了函数包含的参数，和代码块结构，可以通过另一个函数调用执行，也可以用直接用python命令提示符执行。
'''
#定义一个函数


def printme(str):
    "打印任何传入的字符串"
    print(str)
    return

#调用函数


printme("调用函数")
printme("welcome")
