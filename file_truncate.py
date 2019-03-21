#!/usr/bin/python3

fo = open('foo.txt','r+')
print('文件名为：',fo.name)

line = fo.readline()
print("读取行：%s"%(line))

fo.truncate()
line = fo.readlines()
print("读取行：%s"%(line))

fo.close()

fo = open('foo.txt','r+')
print('文件名为：',fo.name)

line = fo.readline()
print("读取行：%s"%(line))

fo.truncate(10)
str = fo.read()
print("读取行：%s"%(str))

fo.close()

