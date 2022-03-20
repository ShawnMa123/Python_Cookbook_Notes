# 有时候不能确定一共有多少个参数，可以使用不定参数，*args

# 例如要计算平均分数，需要去掉一个最高分和最低分
def drop_first_last(grades):
    first, *middle, last = grades
    print(middle)
    return middle


grades_record = [1, 20, 55, 100, 98, 23]
drop_first_last(sorted(grades_record, reverse=True))

# 例如在一个tuple中要将多个参数分解，并赋值给新的变量
record = ('Dave', 'dave@example.ocm', '123456789', '123123123123', 852741963)
name, email, *phone_nubmers = record
print(name)
print(email)
print(phone_nubmers)  # 会自动生成一个list，不管有多少元素个数

# 比较最近一条记录和之前所有记录的平均值
*trailing, current = [10, 8, 510, 515, 551, 85, 2022]
print(trailing)
print(current)

# *args也可以用来分割List[tuple]
records = [('foo', 1, 2), ('bar', 'hello'), ('foo', 3, 4)]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# *args也可以用在字符串操作
line = 'nobody:*:-2:-2:Unprivileged user:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(fields)
print(homedir)
print(sh)

# 如果解压后不需要使用了，可以使用_或者ign
record = ['ACME', 50, 91.1, (12, 18, 2021)]
name, *_, (*_, year) = record
# name, *ign, (*ign, year) = record
# *_ 和 *ign 效果一样
print(name)
print(year)

# 利用*可以快速分割一个list
items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head)
print(tail)


# 可以使用这种方法快速递归
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

# 求出这个list之和
sum(items)
