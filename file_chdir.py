#!/usr/bin/python3

import os,sys

path = '/tmp'

#查看当前工作目录
retval = os.getcwd()
print("当前的工作目录为：%s"%retval)

#修改当前工作目录
os.chdir(path)

newret = os.getcwd()
print('目录修改：%s'%newret)
os.chdir(retval)