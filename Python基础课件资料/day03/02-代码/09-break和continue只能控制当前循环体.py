# 需求:锻炼身体:跑步四圈,做深蹲10分钟,此为一组训练,要做三组
# break 和continue 只能控制本身所在的循环结构
# 在循环嵌套中,外层循环的break和cotinue会影响内层循环, 但是内层循环中的break和continue不会影响外层循环

# 做三组训练的初始状态
i = 1
# 做三组训练后退出循环
while i <= 3:
    print(f'第{i}组训练开始')
    # 跑圈初始状态
    j = 1
    # 跑四圈后退出循环
    if  i== 2:
        print('我女朋友来找我了 先休息一下')
        i += 1
        continue
    while j <= 4:
        print(f'我跑了{j}圈')
        # 内层循环自增变量
        if j ==3 and i == 2:
            print('太累了 休息下')
            break
        j += 1
    print('我做了10分钟深蹲')
    # 外层循环自增变量
    i += 1

