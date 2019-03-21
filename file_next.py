#!/usr/bin/python3

fo = open('foo.txt','r')
print('文件名为：',fo.name)

for index in range(2):
    line = next(fo)
    print('第%d行-%s'%(index,line))

fo.close()