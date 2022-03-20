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
print(phone_nubmers)    # 会自动生成一个list，不管有多少元素个数
