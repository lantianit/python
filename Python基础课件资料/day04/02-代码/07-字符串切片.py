# 切片:就是按照一定的索引位置和步长将字符串分割出一部分就是切片
# 切片的格式:数据序列[起始位置索引:结束位置索引:步长]   字符串,列表,元组,都可以进行切片

str1 = 'itheima'
# 需求:将the切片出来
# 字符串切片以及其他容器类型的切片操作,都会重新生成一个新的数据序列,不会对原有数据序列产生影响
str2 = str1[1:4:1]
print(str2)

# 切片逻辑
# 起始位置: 字符串切片的起点(包含)
# 结束位置:字符串切片的终点(不包含)
# 在开发中绝大多数范围区间是左闭右开区间,其余内容单独记忆(例如 randint是一个闭区间)
# 步长:步长就是每一次查找数据的间隔(相邻两个索引的差值就是步长)

str2 = '我爱北京天安门,天安门上太阳升!'
# 获取"北京天安门"
print(str2[2:7:1])
# 如果步长为1 可以被省略
# 步长省略后,:也可以省略
print(str2[2:7])

# 起始位置也可以省略
# 如果起始位置省略,步长为正数,则起始位置为字符串开始
print(str2[:7:1])  # 我爱北京天安门
# 如果起始位置省略,步长为负数,则起始位置为字符串末尾
print(str2[:7:-1])  # !升阳太上门安天
# 为什么为空?  字符串切片起点 是索引为2 的位置, 步长是-1  切片区间[2,7),此时从2的位置从右向左步长为1 切片此区域没有数据.
print(str2[2:7:-1]) # 空字符串
# 结论: 如果步长是负数,开始位置要在结束位置右侧,否则没有数据

# 结束位置可以省略
# 如果结束位置省略,步长为正数,则结束位置为字符串末尾
print(str2[8::1])  # 天安门上太阳升!
# 下方表达式和上一行是否含义相同? 不相同,因为结束位置写-1不包含结束位置
print(str2[8:-1:1])  # 天安门上太阳升


# 如果结束位置省略,步长为负数,则结束位置为字符串开始
print(str2[8::-1])  # 天,门安天京北爱我
# 如果结束位置写0  含义也不相同
print(str2[8:0:-1])  # 天,门安天京北爱我

# 需求:在字符串中截取"天门天门"
print(str2[4: 11: 2])  # 天门天门
# 在使用字符串切片进行非1步长书写时,要注意起始位置和结束位置,并且查看间隔

# Python中优雅的字符串反转方式
print(str2[::-1])  # !升阳太上门安天,门安天京北爱我

# python中复制数据序列的方法
str3 = str2[:]
print(str3)  # 我爱北京天安门,天安门上太阳升!
