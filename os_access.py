#!/usr/bin/python3

import sys,os

ret = os.access('foo.txt',os.F_OK)
print('F_OK - 返回值%s'%ret)

ret = os.access('foo.txt',os.R_OK)
print('R_OK - 返回值%s'%ret)

ret = os.access('foo.txt',os.W_OK)
print('W_OK - 返回值%s'%ret)

ret = os.access('foo.txt',os.X_OK)
print('X_OK - 返回值%s'%ret)