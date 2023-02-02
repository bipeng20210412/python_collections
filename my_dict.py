"""
date:2023-02-2
time:20:15
author:bipeng
"""


class my_dict(dict):
    def __init__(self, default_factory=None, **kwargs):
        super(my_dict, self).__init__(**kwargs)
        self.default_factory = default_factory

    # 自己实现get函数
    def _get(self, key, default=None):
        if key not in self:
            return default  # 如果不存在key，则返回默认的default
        else:
            return self[key]  # 如果已经存在key，返回key的value值

    # 自己实现setdefalut函数
    def _setdefault(self, key, value):
        if key not in self:  # 如果已经存在key，设置key-value，返回value
            self[key] = value
            return value
        else:
            return self[key]  # 如果已经存在key,返回key的value值

    # __getitem__和__missing__ 是自己实现的defaultdict
    def __getitem__(self, key):
        print('getitem')

        return super().__getitem__(key)

    def __missing__(self, key):  # __getitem__中如果key值不存在，调用__missing__
        print('missing')

        if self.default_factory is None:  # 如果没有设置工厂参数defadefault_factory,返回keyerror

            raise KeyError(key)
        else:
            self[key] = self.default_factory()  # 如果工厂参数defadefault_factory,设置key:default_factory()

            return self.default_factory()

    def __setitem__(self, key, value):
        print('setitem')
        super().__setitem__(key, value)

    def __setattr__(self, key, value):  #实现了字典key可以作为属性

        print('setattr')
        self[key] = value

    def __getattr__(self,key):
        print('getattr')
        return self[key]


dic = my_dict(list, a=1, b=2)
print(dic['g'])
dic.g.append(12)
print(dic)
























