my_list = ["spring", "slook", "strange", "curious", "black", "hope"]

# for i in my_list:
#     # 删除以s开头的元素，
#     if i.startswith("s"):
#         my_list.remove(i)

# 方法一
i = 0
while i < len(my_list):
    if my_list[i].startswith('s'):
        my_list.pop(i)
        continue
    i += 1
# 方法二:
new_list = []
for i in my_list:
    if not i.startswith('s'):
        new_list.append(i)
my_list = new_list

# 方法三:
new_list = []
for i in my_list:
    if i.startswith('s'):
        new_list.append(i)
# print(new_list)

for i in new_list:
    my_list.remove(i)


# # 修改第一个元素为"joke"
# my_list[0] = "joke"
#
# # 获取最后一个元素
# last_one = my_list[-1]
#
# # 将最后一个元素放在joke的后面
# # 因为joke在第0个位置，所以，在下标为1的地方插入最后一个元素
# my_list.insert(1, last_one)

print(my_list)



product = [
    {"name": "电脑", "price": 7000},
    {"name": "鼠标", "price": 30},
    {"name": "usb电动小风扇", "price": 20},
    {"name": "遮阳伞", "price": 50},
]
money = 8000
sum1 = 0  # sum初始化为0，是用来存放总价格

# 通过for取出列表中每一个字典
for dict1 in product:
    # 取出字典中健、值对
    for i in dict1.items():
        if i[0]=='price':
            sum1 += i[1]

print(sum1)
# if money >= sum1:
#     print("能")
# else:
#     print("不能")