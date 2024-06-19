# 需求拆分:
'''
1.展示学生管理系统的功能有哪些,引导用户键入序号选择功能
2.获取用户键入的功能
3.分析具体要执行哪一项功能
4.执行功能
'''


def print_all_option():
    """用户功能界面展示"""
    print('-' * 20)
    print('欢迎登录学员管理系统')
    print('1: 添加学员信息')
    print('2: 删除学员信息')
    print('3: 修改学员信息')
    print('4: 查询学员信息')
    print('5: 遍历输出所有学员信息')
    print('6: 退出系统')
    print('-' * 20)


def choose_option(num):
    """分析要执行哪一项功能"""
    if num == '1':
        print('添加学员')
    elif num == '2':
        print('删除学员')
    elif num == '3':
        print('修改学员')
    elif num == '4':
        print('查询学员')
    elif num == '5':
        print('展示所有学员')
    elif num == '6':
        print('退出程序')
    else:
        print('无此选项,请重新输入')


# # 展示功能界面
# print_all_option()
#
# # 引导用户输入功能序号,并获取序号
# option = input('请输入您要执行功能的序号:')
#
# # 根据获取的序号分析要执行哪些功能
# chose_option(option)


# 思考:学生管理系统,是不是需要输入6  才能退出 不然就一直询问您要输入的选项
# 这中情况下建议使用 while True 构造死循环

while True:
    # 展示功能界面
    print_all_option()

    # 引导用户输入功能序号,并获取序号
    option = input('请输入您要执行功能的序号:')

    # 根据获取的序号分析要执行哪些功能
    choose_option(option)
    input()


# 到现在为止框架已经搭建完成,后续任务就是去填充选项中的功能,比如添加 修改学员等
