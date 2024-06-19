# 需求:用户输入一个文件名,通过文件读写操作进行文件备份,并且将备份文件名称更改为:源文件名[备份].后缀

# 1.获取用户键入的文件名
# 2.要通过文件读写操作进行备份
#   2.1.拼接备份后的文件的文件名
#   2.2.读取源文件
#   2.3.写入新文件

# 1.获取用户键入的文件名
file_name = input('请输入您要备份的文件名称:')
file = open(file_name, 'r', encoding='utf-8')
# 2.要通过文件读写操作进行备份
# 2.1.拼接备份后的文件的文件名
copy_file_name = file_name.replace('.', '[备份].')
# 打开新文件
# 如果不是多次打开关闭文件,在一次打开过程中,多次写入,可以持续写入
# 但是如果下次打开该文件会将文件清空
copy_file = open(copy_file_name, 'w')
# copy_file = open(copy_file_name, 'a')
# # 读取旧文件数据
# content = file.read()
# # 写入新文件
# copy_file.write(content)
# 一般情况下,文件都是指定单次读取的最大字符的
# 循环进行读取并写入,直到所有字符读取完成
while True:
    content = file.read(3)
    if content == '':
        break
    copy_file.write(content)

# 关闭文件
file.close()
copy_file.close()

