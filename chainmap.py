"""
date:2023-01-19
time:13:58
author:bipeng
"""

from collections import ChainMap

father = {"father": 1}
mother = {"mother": 2}
family = ChainMap(father, mother)

inner = family.maps
print(inner)

family.update({"friend_1": 3}, friend_2=4)
print(family)

"""
结果为ChainMap({'father': 1, 'friend_1': 3, 'friend_2': 4}, {'mother': 2}) 
只对第一个映射改变，其他操作也只会影响第一个映射
"""

print(father)  # 结果为{'father': 1, 'friend_1': 3, 'friend_2': 4}外部的father也会跟着改变

child_1 = {"child_1": 5}
child_2 = {"child_2": 6}

new_family = family.new_child(child_1)
print(family is new_family)  # 结果为False，用new_child新生成了一个ChainMap
print(new_family)  # 结果为ChainMap({'child_1': 5}, {'father': 1, 'friend_1': 3, 'friend_2': 4}, {'mother': 2})

new_family_2 = family.new_child(child_2)
print(new_family_2)

"""
结果为:ChainMap({'child_2': 6}, {'father': 1, 'friend_1': 3, 'friend_2': 4}, {'mother': 2})
会用child_2替换child_1的位置，也就是把child_1删除，把child_2放到child_1的位置
"""

print(new_family.parents)  # 结果为ChainMap({'father': 1, 'friend_1': 3, 'friend_2': 4}, {'mother': 2})
print(new_family.parents.parents)  # 结果为ChainMap({'mother': 2})


"""
总结:
1:ChainMap不会将其映射合并在一起。相反，它将它们保存在一个内部映射列表中。通过maps获取内部映射列表，通过内部映射列表按顺序搜索键

2：导入映射变化后会导致ChainMap变化，但ChainMao仅对内部列表中的所有只对第一个映射执行有影响，
ChainMap实现了dict的很多方法，使用方法跟dict一样。

3:




"""
