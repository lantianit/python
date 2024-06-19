# break 打破循环,后续循环不会执行
str1 = 'itheima'
for i in str1:
    if i == 'e':
        print('遇到e了,结束循环')
        break
    print(i)

# continue 跳出本次循环,进入下一次循环,不会影响循环次数
str1 = 'itheima'
for i in str1:
    if i == 'e':
        print('遇到e了,进入下一次循环')
        continue
    print(i)

'''
案例：用for循环实现用户登录
① 输入用户名和密码
② 判断用户名和密码是否正确（username='admin'，password='admin888'） 
③ 登录仅有三次机会，超过3次会报错 
'''
# 循环三次
for i in range(3):
    # 获取用户名和密码
    username = input('请输入您的用户名:')
    password = input('请输入您的密码:')
    # 比对用户名和密码
    if username == 'admin' and password == 'admin888':
        print('登录成功')
        break
    else:
        print('用户名或密码错误')
    if i == 2:
        print('三次机会已经用完,账号被冻结')