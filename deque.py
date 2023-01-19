from collections import deque

res = deque(["a", "b", "c"])
print(res)

res.append("right_1")  # 向右端添加
res.appendleft("left_1")  # 向左端添加

res.extend(["right_2", "right_3"])
res.extendleft(["left_2", "left_3"])
# 结果为deque(['right_3', 'right_2', 'left_1', 'a', 'b', 'c', 'right_1', 'right_2', 'right_3'])
# 向左添加时从左取内容，一个一个放到左边


res.pop()  # 从右端出队
res.popleft()  # 从左端出队

res.reverse()  # 反转队列

res.rotate(2)  # 依次从右端取数，放在左端
res.rotate(-2)  # 依次从左端取数，放在右端

print(res)

# **********************************************************************************


res1 = deque([1, 2, 3, 4, 5], maxlen=5)  # 最大长度为5
res1.append(6)  # 队列满时，继续往队列右边append，会把最左端的数给挤出去
print(res1)  # 结果为deque([2, 3, 4, 5, 6], maxlen=5)

"""
1:deque 是Python标准库 collections 中的一个类，实现了两端都可以操作的队列，相当于双端队列，与Python的基本数据类型列表很相似。
2:deque 有一些方法和list一样，用法也一样。

"""
