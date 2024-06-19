# 需求拆分:
'''
1.展示学生管理系统的功能有哪些,引导用户键入序号选择功能
2.获取用户键入的功能
3.分析具体要执行哪一项功能
4.执行功能
'''

# 用户功能界面展示
print('-' * 20)
print('欢迎登录学员管理系统')
print('1: 添加学员信息')
print('2: 删除学员信息')
print('3: 修改学员信息')
print('4: 查询学员信息')
print('5: 遍历输出所有学员信息')
print('6: 退出系统')
print('-' * 20)

# 引导用户输入功能序号,并获取序号
option = input('请输入您要执行功能的序号:')
print(option)

# 分析要执行哪一项功能
# 执行功能
if option == '1':
    print('添加学员')
elif option == '2':
    print('删除学员')
elif option =='3':
    print('修改学员')
elif option == '4':
    print('查询学员')
elif option == '5':
    print('展示所有学员')
elif option == '6':
    print('退出程序')
else:
    print('无此选项,请重新输入')



