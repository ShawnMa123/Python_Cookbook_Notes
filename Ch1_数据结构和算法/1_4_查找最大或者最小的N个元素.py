# 从一个集合中获取最大或者最小的N个元素
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# nlargest可以获取最大的N个元素
print(heapq.nlargest(3, nums))
# nsmallest可以获取最小的N个元素
print(heapq.nsmallest(3, nums))

# nlargest和nsmallest可以接受一些额外关键字参数
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
print(f"cheap is {cheap}")
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(f"expensive is {expensive}")

