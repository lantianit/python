# 牛奶和可乐交换的案例
'''
交换方式:
获取一个空杯子
将牛奶倒入空杯子
将可乐倒入原牛奶现空杯子的杯子中.....
'''

'''
换一个方式进行描述:
# 开始
A杯子: 牛奶
B杯子: 可乐
C杯子: 空
# 过程
A >> C
B >> A
C >> B
# 结尾
A杯子: 可乐
B杯子: 牛奶
C杯子: 空
'''

a = '牛奶'
b = '可乐'
c = '空'
print(a, b)

c = a
a = b
b = c

print(a, b)

# 关键字: 系统定义的具有一定功能或者含义的字符组合.(关键字不要背诵,遇到了就记下来,如果记不下来,关键字有自己的高亮效果)
# 标识符: 程序员自己定义的具有一定功能或者含义的字符组合.

# 标识符的命名规则:
# 1/只能由数字,字母,下划线组成
# 2/首字母不能是数字
# 3/不能是关键字
# 4/严格区分大小写

# 什么地方使用了标识符:文件名,变量名, 函数名, 类型名  (只要是让程序员起名字,都是标识符)
# 文件名可以不遵循标识符的命名规则,但是在服务器中无法使用,不能当做模块进行导入,很多服务器工具或组件不支持非标识符文件.

'''
Python)abc  不能
_abc   可以
anc______  可以
123abc _____  不可以
and  不可以
ABC  可以
anc  可以
'''

# 在windows中文件名定义时,不严格区分大小写
# 程序员不可能定义变量出错

# aaa
# 在Python中创建变量必须赋值,否则将会报错