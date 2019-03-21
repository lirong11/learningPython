#!/usr/bin/python3

#打开文件
fo = open('foo.txt','wb')
print('文件名为：',fo.name)

fid = fo.fileno()
print('文件描述为：',fid)

#关闭文件
fo.close()