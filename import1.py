#从某个模块中导入某个函数，格式为： from somemodule import somefunction

from sys import argv,path #导入特定成员

print('=========python from import===========')
print('path:',path)#因为已经导入path成员，所以此处引用不需要加sys.path