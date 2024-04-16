import traceback

class AgeError(Exception):
    def __int__(self, errorinfo):
        Exception.__init__(self)
        self.errorinfo = errorinfo
    def __str__(self):
        return str(self.errorinfo)+"年龄错误"
if __name__ == '__main__':
    age = int(input("输入一个年龄"))
    if age < 1 or age > 150:
        raise AgeError(age)
    else:
        print("年龄正常")

# try:
#     print("step1")
#     num = 1/0
# except:
#     with open("xxx") as f:
#         traceback.print_exc(file = f)

# try:
#     print("step1")
#     num = 1/0
# except:
#     traceback.print_exc()

# with open("xxx") as f:
#     for line in f:
#         print(line)

# try:
#     f = open("d:/a","r")
#     content = f.readline()
#     print(content)
# except BaseException as e:
#     print(e)
# finally:
#     print("出现异常是否走到这里1")
#     f.close()
#
# print("出现异常是否走到这里2")

# while True:
#     try:
#         a = input("请输入除数：")
#         b = input("请输入被除数: ")
#         c = float(a) / float(b)
#         print(c)
#
#     except ZeroDivisionError:
#         print("异常：被除数不能为0")
#     except TypeError:
#         print("异常，除数和被除数都应该为整数")
#     except BaseException as e:
#         print(e)
#         print(type(e))

# while True:
#     try:
#         x = int(input("请输入一个数："))
#         print("您输入的数是：",x)
#         if x == 88:
#             print("退出程序")
#             break
#     except:
#         print("异常，您输入的不是数字")
