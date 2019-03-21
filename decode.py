#!/user/bin/python3

str = "菜鸟教程";
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")

print(str)

print("UTF-8编码：",str_utf8)
print("GBK编码：",str_gbk)

print("UTF-8解码：",str_utf8.decode('UTF-8','strict'))
print("GBK编码：",str_gbk.decode('GBK','strict'))