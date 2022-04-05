# 对一个dict进行一些计算操作，例如max min sort

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

print(prices['ACME'])

# 取max或者min的value
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

# 对字典进行排序
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

# zip() 只能访问一次
price_and_name = zip(prices.values(), prices.keys())
print(min(price_and_name))
# print(max(price_and_name


# 直接对字典进行运算，实际上是对key进行操作
print(min(prices))
print(max(prices))

# 根据value筛选对应的key
print(min(prices, key=lambda k: prices[k]))
print(max(prices, key=lambda k: prices[k]))
# 如果需要最小值的value，需要额外进行操作
min_value = prices[min(prices, key= lambda k : prices[k])]
print(min_value)
