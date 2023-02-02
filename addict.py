"""
date:2023-02-2
time:22:15
author:bipeng
"""



from addict import Dict as di

dic = {}
dic_x = di()

# 1
print(dic_x.d)  # 对于不存在的key，返回一个空字典。类似defalultdict

# 2 可以嵌套调用
dic_x.a.b = 1
dic_x.a.c = 2

print(dic_x)  # 结果为{'a': {'b': 1, 'c': 2}}

# 3
dic_1 = {'a': [{'b': 3}, {'b': 3}]}
dic_x1 = di(dic_1)
print(dic_x1.a is dic_1['a'])  # 结果为False

# 4 addict 不会让你覆盖 dict 的属性，因此以下操作将不起作用：

dic_x2 = di()
# dic_x2.keys = 12
# dic_x2.pop = 13
# 不能用普通dict的函数名当属性名

# 5 可以转化为普通字典
print(dic_x1.to_dict())

# 6
data = [
    {'born': 1980, 'gender': 'M', 'eyes': 'green'},
    {'born': 1980, 'gender': 'F', 'eyes': 'green'},
    {'born': 1980, 'gender': 'M', 'eyes': 'blue'},
    {'born': 1980, 'gender': 'M', 'eyes': 'green'},
    {'born': 1980, 'gender': 'M', 'eyes': 'green'},
    {'born': 1980, 'gender': 'F', 'eyes': 'blue'},
    {'born': 1981, 'gender': 'M', 'eyes': 'blue'},
    {'born': 1981, 'gender': 'F', 'eyes': 'green'},
    {'born': 1981, 'gender': 'M', 'eyes': 'blue'},
    {'born': 1981, 'gender': 'F', 'eyes': 'blue'},
    {'born': 1981, 'gender': 'M', 'eyes': 'green'},
    {'born': 1981, 'gender': 'F', 'eyes': 'blue'}]

dic_x3 = di()
for row in data:
    born = row['born']
    gender = row['gender']
    eyes = row['eyes']

    dic_x3[born][gender][eyes] += 1

print(dic_x3)

# 7 []和 .的区别
dic_x4 = di()

name = "bipeng"
dic_x4.name = 12
print(dic_x4)  # 结果为{'name': 12}
dic_x4[name] = 12  # 结果为{'name': 12, 'bipeng': 12}
print(dic_x4)  # 结果为{'name': 12, 'bipeng': 12}

#[]会拿字符串的值bipeng当key。而.是拿字符串name当key
