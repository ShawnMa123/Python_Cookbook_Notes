# 想构造一个字典，其中一个key可以映射多个value
# d = {'a': [1, 2, 3],
#      'b': [4, 5]}
# e = {
#     'a': {1, 2, 3},
#     'b': {4, 5}
# }


# defaultdict会自动初始化每个key对应的value
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(3)
print(d)

# defaultdict会自动为key创建实体，就算这个key不存在
# 如果不需要这样子，可以对一个dict使用setdefault()
d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d)


# 假如不使用上面的方法
d1 = {}
for key, value in paris:
    if key not in d:
        d1[key] = []
    d1[key].append(value)


# 使用defaultdict会更加简单
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)