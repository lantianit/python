# 打印一个直角三角形

for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{j} * {i} = {i * j}', end='\t')
    print()

# 在for循环之外还可以调用i 或者j 么? 能

# 在Python中for循环中创建的临时变量可以被外界调用,但是不要用
# print(i)
# print(j)
# 使用for循环临时变量可能会出现报错
# for i in range(1,1):
#     print(123)

# 当for循环执行后,没有一次进入循环体内,也就是遍历的序列是一个空序列,那么临时变量将不会被定义,所以不要使用
# NameError: name 'i' is not defined
# print(i)
