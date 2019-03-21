#!/usr/bin/python3

#传不可变参数
def ChangeInt(a):
    print("a = ",a)
    a = 10
    print("ChangeInt a = ",a)

b = 2
ChangeInt(b)
print("b = ",b)
#有 int 对象 2，指向它的变量是 b，在传递给 ChangeInt 函数时，按传值的方式复制了变量 b，a 和 b 都指向了同一个 Int 对象，在 a=10 时，则新生成一个 int 值对象 10，并让 a 指向它


#传可变参数
def changeme(mylist):
    print("mylist : ",mylist)
    mylist.append([1,2,3,4])
    print("changeme mylist:",mylist)
    return

list = [10,20,30]
print("list：",list)
#调用changeme函数
changeme(list)
print("函数外取值：",list)