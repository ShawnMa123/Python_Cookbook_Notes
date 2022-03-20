from collections import deque

# deque(maxlen=N)可以构造一个固定大小的队列
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)

q.append(4)
print(q)

q.append(5)
print(q)

# 不设置maxlen的话，可以得到无限长度的deque队列
q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)

q.appendleft(4)
print(q)

q.pop()
print(q)
q.popleft()
print(q)
# 在队列两端插入或者删除是O(1)，但是对list操作的话是O(N)


x = [1, 2, 3, 4, 5]
x.insert(5,11)
print(x)
x_deque = deque(x)
print(x_deque)
x_deque.append(55)
print(x_deque)
