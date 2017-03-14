# /usr/bin/env python
# coding=utf-8

# 问题 包含N个元素的元祖和序列，如何同时解压赋值给N个变量

# 解决方案 在python中任何序列或可迭代对象都可以通过简单的语句来实现，前提是变量数量要和序列元素数量要一致
# 代码示例

p = (4, 5)
x, y = p
print x, y
# >>> 4, 5
data = ['acme', 50, 90.1, (2012, 12, 30)]
name, shares, price, date = data
print name, date
# >>> 'acme' (2012, 12, 30)
# 可迭代对象的解压
name, shares, price, (year, month, day) = data
print shares, price, year
# >>> 50 90.1 2012

# 若变量个数与序列元素个数不一致，会抛出异常
# name, shares, price, date, discount = data
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: need more than 4 values to unpack


