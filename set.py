student = {'Tom','Jim','Mary','Tom','Jack','Rose'}
print(student) #输出集合，重复的元素被自动去掉

#成员测试
if 'Rose' in student :
    print('Rose在集合中')
else:
    print('Rose不在集合中')

#set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
c = set("\'abc\'\,\'csf\'")

print(a)
print(len(a))
print(c)
print(len(c))

print(a-b) #a和b的差集
print(a|b) #a和b的并集
print(a&b) #a和b的交集
print(a^b) #a和b中不同时存在的元素

print(len(a))

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

thisset = set(("Google", "Runoob", "Taobao"))
thisset.add("Facebook")
print(thisset)

thisset = set(("Google", "Runoob", "Taobao"))
thisset.update({1,3})
print(thisset)

thisset.update([1,4],[5,6])
print(thisset)

thisset = set(("Google", "Runoob", "Taobao"))
thisset.remove("Taobao")
print(thisset)
thisset.remove("Facebook") # 不存在会发生错误

thisset = set(("Google", "Runoob", "Taobao"))
thisset.discard("Facebook") # 不存在不会发生错误
print(thisset)

thisset = set(("Google", "Runoob", "Taobao", "Facebook"))
x = thisset.pop()
print(x)

