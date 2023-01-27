"""
date:2023-01-27
time:21:25
author:bipeng
"""

# 我们是使用namedtuple生成类，而不是对象
from collections import namedtuple

# 生成类(第2个参数有两种写法）
User = namedtuple("User", ["name", "age", "height"])
User1 = namedtuple("User", 'name age height')
User2 = namedtuple("User", ["name", "class", "height"], rename=True, defaults=[1, 2, 3])
# 当字段名有python关键字时，rename必须为True。否则就报错。# ValueError: Type names and field names cannot be a keyword: 'class'
# 当defaults参数设置时，才有_fields_default这个属性。就相当于给字段设置默认值

# 根据类创建命名实例(3种方式)
user = User(name="BIPENG", age=33, height=171)
user1 = User("BIPENG", 33, 171)
user2 = User._make(["BIPENG", 33, 171])  # 可以用_make函数给nametuple赋值

user3 = user._replace(age=12)  # 更新age,重新生成一个nametuple.并赋值给user3
print(user3)  # 结果为User(name='BIPENG', age=12, height=171)
print(user3._fields)  # 返回user3的字段。('name', 'age', 'height')

# 我们可以使用点获得属性值
print(user.age, user.name, user.height)
print(user[1])  # 还可以用下标来获取对象啊

# nametuple可以转化为字典
dict1 = user3._asdict()
print(dict1)  # 结果为{'name': 'BIPENG', 'age': 12, 'height': 171}

# user3._source
# user3._field_types
# 这两个函数已经取消。存在的目的可能是为了向后兼容


# tuple有的方法和特性,nametuple也有,因为nametuple是tuple的子类

name, age, height = user3  # unpack 拆包
