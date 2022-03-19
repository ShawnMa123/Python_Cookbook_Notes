# 对于序列和其他可迭代对象，可以通过赋值来解压并且把他们分配给多个变量
# 前提是变量个数和元素个数相等

p = (4, 5)
print(type(p))

x, y = p
print(x)
print(y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
print(type(data))

name, shares, price, date = data
print(name)
print(shares)
print(price)
print(date)


# str 也支持这样的解压赋值操作
s = 'Hello'
a, b, c, d, e = s
print(a)
print(b)
print(c)
print(d)
print(e)


# 对于只需要部分解压的场景，可以使用 _ 来进行占位
data = ['ACME', 50, 91.1, (2012, 12, 21)]
# 这样就只取到中间的两个值
_, shares, price, _ = data
print(shares)
print(price)
