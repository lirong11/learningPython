#!/usr/bin/python3

fo = open('foo.txt','wb')
print('文件名为：',fo.name)

#刷新缓冲区
fo.flush()

#关闭文件
fo.close()

