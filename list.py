#!/usr/bin/python3

list1, list2 = ['Google', 'Taobao', 'Runoob'], [456, 700, 200]

print ("list1 最小元素值 : ", min(list1))
print ("list2 最小元素值 : ", min(list2))

print ("list1 最大元素值 : ", max(list1))
print ("list2 最大元素值 : ", max(list2))

aTuple = (123, 'Google', 'Runoob', 'Taobao')
list1 = list(aTuple)
print ("Tuple列表元素 : ", list1)

str="Hello World"
list2=list(str)
print ("string列表元素 : ", list2)