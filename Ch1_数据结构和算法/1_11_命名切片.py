######    0123456789012345678901234567890123456789012345678901234567890'
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])

print(cost)

# 可以直接对切片进行命名，下次直接调用
shares = slice(20, 23)
price = slice(31, 37)
cost_new = int(record[shares]) * float(record[price])
print(f'cost = {cost_new}')

# slice() 可以创建切片对象
items = [0, 1, 2, 3, 4, 5]
a = slice(2, 4)
print(items[2:4] == items[a])

b = slice(5, 20, 2)
print(b.start)
print(b.stop)
print(b.step)

s = 'HelloWorld'
# 在直接使用切片时，会自动调整到适用的边界值，不会出现Indexerror
print(b.indices(len(s)))
for i in range(*b.indices(len(s))):
    print(s[i])
