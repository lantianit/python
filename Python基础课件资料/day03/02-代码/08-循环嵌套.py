# 需求:锻炼身体:跑步四圈,做深蹲10分钟,此为一组训练,要做三组
# 在循环嵌套中,外层循环执行一次,内层循环全部执行完成
# 做三组训练的初始状态
i = 1
# 做三组训练后退出循环
while i <= 3:
    print(f'第{i}组训练开始')
    # 跑圈初始状态
    j = 1
    # 跑四圈后退出循环
    while j <= 4:
        print(f'我跑了{j}圈')
        # 内层循环自增变量
        j += 1
    print('我做了10分钟深蹲')
    # 外层循环自增变量
    i += 1