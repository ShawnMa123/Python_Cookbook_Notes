# 在迭代中可以控制字典元素的顺序
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])

import json

a = json.dumps(d)
print(a)
print(type(a))

