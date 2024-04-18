

# with open("b.txt","r",encoding="utf-8") as f:
#     lines = f.readlines()
#     lines2 = [line.rstrip() + "#" + str(index) + "\n" for index,line in zip(range(1,len(lines)+1),lines)]

# with open("b.txt","r",encoding="utf-8") as f:
#     lines = f.readlines()
#     lines2 = [line.rstrip()+"#"+str(index)+"\n" for index,line in zip(range(1,len(lines)+1),lines)]

# with open(r"a.txt","r") as f:
#     for a in f:
#         print(a,end="")

# with open(r"a.txt","r") as f:
#     while True:
#         fragment = f.readline()
#         if not fragment:
#             break
#         else:
#             print(fragment,end="")

# with open(r"a.txt","r",encoding="utf-8") as f:
#     print(f.read())

# s = [r"123\n","456"]
# with open(r"a.txt","w") as f:
#     f.writelines(s)

# s = {"123"}
# print(type(s))

# try:
#     f = open(r"my01.txt","a")
#     s = "12"
#     f.write(s)
# except BaseException as e:
#     print(e)
# finally:
#     f.close()

# f = open("d.txt","w",encoding="utf-8")
# f.write("你好\n")
# f.close()

# with open(r"a.txt","a") as f:
#     s = r"\n123\n"
#     f.write(s)

# f = open(r"a.txt","a")
# s = "123"
# f.write(s)
# f.close()