from collections import Counter

my_list = Counter(["a", "b", "a", "a", "c", "d", "a", "b", "c", "a", "d"])

res = Counter(my_list)
print(res)  # 结果为Counter({'a': 5, 'b': 2, 'c': 2, 'd': 1}) 统计完毕

print(res.total())  # 结果为11  返回my_list的长度

print(res.most_common(2))  # 结果为[('a', 5), ('b', 2)]，返回出现频率最高的两个结果

res.subtract("a")
print(res)  # 结果为Counter({'a': 4, 'b': 2, 'c': 2, 'd': 1}),将a的数量减去了1


res["a"]=23



"""
1:Counter() 是 collections 库中的一个函数，可以用来统计一个 python 列表、字符串、元组等可迭代对象中每个元素出现的次数，并返回一个字典
2:Counter提供了一些普通dict的函数。和普通的dict方法没什么区别
"""
