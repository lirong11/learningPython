#!user/bin/python3

dict = {'Name':'Runoob','Age':7,'Class':'Frist'}

print("dict['Name']:",dict['Name'])
print("dict['Age']:",dict['Age'])

dict['Age'] = 8; #更新Age
dict['School'] = "菜鸟教程" #添加信息

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

print(dict)
del dict['Name'] #删除键'Name'
print(dict)

dict.clear()#清空字典
print(dict)

del dict #删除字典
