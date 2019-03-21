#!/usr/bin/python3

fo = open('foo.txt','wb')
print('文件名为：',fo.name)

ret = fo.isatty()
print('返回值：',ret)

fo.close()