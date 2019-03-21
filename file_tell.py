#!/usr/bin.python3

fo = open('foo.txt','r+')
print('文件名为：',fo.name)

line = fo.readline()
print('数据读取的位置是：%s'%(line))

#获取当前文件的位置
pos = fo.tell()
print("当前位置：%d"%(pos))

fo.close()