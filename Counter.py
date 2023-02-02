from collections import Counter

my_list = Counter(["a", "b", "a", "a", "c", "d", "a", "b", "c", "a", "d"])

res = Counter(my_list)
print(res)  # 结果为Counter({'a': 5, 'b': 2, 'c': 2, 'd': 1}) 统计完毕

print(res.total())  # 结果为11  返回my_list的长度

print(res.most_common(2))  # 结果为[('a', 5), ('b', 2)]，返回出现频率最高的两个结果

res.subtract("a")
print(res)  # 结果为Counter({'a': 4, 'b': 2, 'c': 2, 'd': 1}),将a的数量减去了1


print(dict(res)) #Counter可以变为普通dict



"""
1:Counter() 是 collections 库中的一个函数，可以用来统计一个 python 列表、字符串、元组等可迭代对象中每个元素出现的次数，并返回一个字典
2:Counter提供了一些普通dict的函数。和普通的dict方法没什么区别
"""



"""
date:2023-02-2
time:22:52
author:bipeng
"""

# 加减运算

st = "aabbccdd"
st1 = 'abcd'

cnt1 = Counter(st)
cnt2 = Counter(st1)

cnt1.update(cnt2)  # 加法   等价于cnt1+=cnt2
# cnt1+=cnt2
print(cnt1)  # 结果为Counter({'a': 3, 'b': 3, 'c': 3, 'd': 3})

cnt2.subtract(cnt1)  # 减法
print(cnt2)  # 结果为Counter({'a': -2, 'b': -2, 'c': -2, 'd': -2})

# 集合运算
cnt3 = Counter("abbbcdfi")
cnt4 = Counter("aabccde")

print(cnt3 | cnt4)  # 并集 Counter({'b': 3, 'a': 2, 'c': 2, 'd': 1, 'f': 1, 'i': 1, 'e': 1}) 取value大的
print(cnt3 + cnt4)  # 求和 Counter({'b': 4, 'a': 3, 'c': 3, 'd': 2, 'f': 1, 'i': 1, 'e': 1})
print(cnt3 - cnt4)  # 差集 Counter({'b': 2, 'f': 1, 'i': 1})   从cnt3中每个key进行相减，不显示差集运算后<=0的项目
print(cnt3 & cnt4)  # 交集 Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1})  取value小的



