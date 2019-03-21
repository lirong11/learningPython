#!/usr/bin/python3

#import sys引入python标准库中的sys.py模块
import sys

print('命令行参数如下')
#sys.argv是一个包含命令行参数的列表
for i in sys.argv:
    print(i)

#sys.path包含一个python解释器自动查找所需模块的路径的列表
print('\n\npython 路径为：',sys.path,'\n')