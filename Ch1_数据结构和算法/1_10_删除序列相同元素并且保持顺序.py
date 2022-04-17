# 如果序列的值都是hashable
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))


# 假如元素是不可哈希的 例如dict
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
# 将dict的key和value都作为去重的filter
res = list(dedupe(a, key=lambda d: (d['x'], d['y'])))
print(res)
# 将dict的key作为去重的filter
res = list(dedupe(a, key=lambda d: (d['x'])))
print(res)