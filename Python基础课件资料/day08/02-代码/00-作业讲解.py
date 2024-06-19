# 定义函数find_all_pos，实现找出列表中某个元素所有位置的起始下标，要求返回符合要求的所有位置的起始下标，如`[3, 6, 1, 4, 1, 5, 6, 1, 3, 6, 2]`，需要找出里面所有的`1`的位置，最后将返回一个元组`(2, 4, 7)`

def find_all_pos(num_list, sub_num):
    # list1.index(1) 使用这种方法查找,得到的是从左至右第一次出现的下标位置
    # 使用index查找,如果没找到则会报错,所以我们只循环指定元素出现的次数
    # 创建起始位置
    start_index = 0
    # 创建一个空列表,用于储存每次查询到的索引
    index_list = []
    # 循环数字出现的次数,否则可能index会报错
    for i in range(num_list.count(sub_num)):
        # 查询索引
        index = num_list.index(sub_num, start_index)
        # 将索引放入index_list
        index_list.append(index)
        # 更新下次查询的起始位置
        start_index = index + 1
    # 将索引以元组的形式返回
    return tuple(index_list)



list1 = [3, 6, 1, 4, 1, 5, 6, 1, 3, 6, 2]

num = 1

print(find_all_pos(list1, num))



index_list = []
for index, value in enumerate(list1):
    if value == num:
        index_list.append(index)

print(index_list)


# 斐波那契数列：1，1，2，3，5，8... 即前两个数字是1, 从第三个数字开始，每个数字是前两个数字之和，编写函数，输出n个数的斐波那契数列
'''
f(1) = 1
f(2) = 1
f(3) = f(1) + f(2)
f(4) = f(3) + f(2)
f(5) = f(4) + f(3)
.....
f(n) = f(n-1) + f(n-2)
'''

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_list(n):
    list1 = []
    for i in range(1, n+1):
        list1.append(fibonacci(i))
    return list1


print(fibonacci(20))
print(fibonacci_list(10))




















