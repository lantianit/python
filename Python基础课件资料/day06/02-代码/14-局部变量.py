# 在函数体内部定义的变量,出了函数体就会被释放掉
def sum1():
    a = 1
    b = 2
    print(a + b)

sum1()
# 思考? 我们再函数体外部可以调用a, b 么?
# NameError: name 'a' is not defined  函数体内部定义的变量,出了函数体救护被释放掉
# print(a + b)