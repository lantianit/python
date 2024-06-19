# 求 1-100的累加和
sum1 = 0
for i in range(1, 101):
    sum1 += i
print(f'1-100的累加和为{sum1}')

# 求1-100的偶数累加和
sum1 = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum1 += i

print(f'1-100的偶数累加和为{sum1}')

# 求1-100的偶数累加和
# 在开发中尽量不要这样写 相当于人脑计算了规律,让代码按照人脑捕获的规律执行
# sum1 = 0
# for i in range(0, 101, 2):
#     sum1 += i
#
# print(f'1-100的偶数累加和为{sum1}')
