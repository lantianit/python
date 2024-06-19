  

## 题目1

新建一个文件，写入“人生苦短，我用Python”，然后将这个文件中的数据读取出来，打印到控制台



**参考答案**

```python
# 写文件
f1 = open("xxx.txt", "w", encoding="utf-8")  # 只写方式打开文件
f1.write("人生苦短，我用python")  # 往文件写内容
f1.close()  # 关闭文件

# 读文件
f2 = open("xxx.txt", "r", encoding="utf-8")  # 只读方式打开
content = f2.read()  # 读取文件的内容
print(content)  # 打印读取到的内容
f2.close()  # 关闭文件
```

