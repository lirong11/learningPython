#!/usr/bin/python3

f = open("foo.txt","w")
num = f.write("Python是一个非常好的语言。\n是的，的确很好！！\n")
print(num)
f.close()

f = open('foo.txt','r')
str = f.read()
print(str)
str = f.readline()
print('=========')
print(str)
f.close()

f = open('foo.txt','r')
str = f.readline()
print('=========')
print(str)
f.close()


f = open('foo.txt','r')
str = f.readlines()
print('=========')
print(str)
f.close()

f = open('foo.txt','r')
print('=========')
for line in f:
    print(line,end='')
f.close()

