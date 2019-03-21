#!/usr/bin/prthon3

import support
import using_name

support.print_func('leerong')

print('{name}网址：{site}'.format(name ='leerong',site = 'www.leerong.com'))

print('{0}和{1}'.format('hello','hi'))
print('{1}和{0}'.format('hello','hi'))

for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),end=' ')
    print(repr(x*x*x).rjust(4))

for x in range (1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))