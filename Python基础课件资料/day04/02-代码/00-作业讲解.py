# 过7游戏
# 需求: 叔叔,1-100  凡是7 和 7的倍数,以及数字中带7的所有数字, 输出 哈  否则 输出数字
# 获取十位数字:  i // 10 == 7
# 获取各位数字:  i % 10 == 7
# for i in range(1, 101):
#     if i % 7 == 0 or i % 10 == 7 or i // 10 == 7:
#         print('哈')
#     else:
#         print(i)


# 需求: 1-1000  获取 各位 十位 百位
# 个位: i %10 == 7
# 十位: i // 10 % 10 = 7
# 百位: i // 100 == 7




# 从键盘上输入一个字母，判断此字母 是否在变量 a 中，
# 如果在则输出 找到了， 如果不在 则输出 查无此字母
# a = 'itheima'
# char1 = input('请输入一个字母:')
# for i in a:
#     if i == char1:
#         print('找到了')
#         break
# else:
#     print('查无此字母')

a = 'itheaima'
index = 0
char1 = input('请输入一个字母:')
for i in a:
    if i == char1:
        print('找到了')
        break
    index += 1
    if index == len(a):
        print('查无此字母')

