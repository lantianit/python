# day10 每日练习题

## 当天知识点回顾

* 多态

  * 理解相对较难，比较抽象

* 类属性和实例属性

  * 类属性：类拥有的属性
  * 实例属性：实例对象拥有的属性

* 实例方法、类方法、静态方法

  * 实例方法
    * 实例对象拥有的方法
  * 类方法
    * 使用classmethod修饰器修饰
    * 类拥有的方法，第一个参数是cls
  * 静态方法
    * 使用staticmethod装饰器修饰
    * 相当于一个普通的方法

* 异常

  * 什么是异常

    * 程序中出现的不正常
    * 比如0/1

  * 异常的捕获

    ~~~python
    try:
        # 需要捕获的异常
        pass
    except:
        # 有异常抛出的异常
        pass
    else:
        # 没有异常执行
        pass
    finally:
        # 有没有异常都会执行
        pass
    ~~~

  * 异常的传递

    * 由里往外传

  * 自定义异常

    * 继承Exception

  * 抛出异常

    * raise


## 随堂练习

* 多态案例
* 类属性，实例属性案例
* 类方法、静态方法、实例方法的使用
* 异常案例



## 每日练习

**题目1（代码题）**

**要求：**

使用类属性、类方法的知识实现以下功能：

- 创建一个学生类`Student`，每创建一个对象自动实现学生个数累加，学生总分自动累加

  - 类属性有

  ```python
      num = 0  # 学生个数
      total_score = 0  # 学生总分
  ```

  - 学生基本属性有姓名、分数

- 设计`__str__`方法，返回学生的基本属性

- 设计几个类方法，分别返回学生个数、学生总分、班级平均分

**训练提示**

* 类方法
  * classmethod

**运行结果：**

~~~
班级总人数为： 0
学生姓名:mike, 考试分数:59
学生姓名:yoyo, 考试分数:88
学生姓名:rock, 考试分数:98
班级总人数为： 3
班级总分为： 245
班级平均分为：81.67
~~~

**参考答案**

~~~python
class Student(object):
    num = 0  # 学生个数
    total_score = 0  # 学生总分

    def __init__(self, name, score):
        self.name = name  # 学生名字
        self.score = score  # 分数

        # 每实例化一个对象
        # 学生个数自动累加1
        Student.num += 1
        # 学生总分累加
        Student.total_score += score

    def __str__(self):
        return f'学生姓名:{self.name}, 考试分数:{self.score}'

    # 类方法，返回学生个数
    @classmethod
    def get_stu_num(cls):
        return cls.num

    # 类方法，返回班级总分
    @classmethod
    def get_total_score(cls):
        return cls.total_score

    # 类方法，返回班级平均分
    @classmethod
    def get_avg_socre(cls):
        avg = 0
        if cls.num != 0:  # 人数不为0求平局分才有意义
          	# 平均分 = 总分/总人数
            avg = cls.total_score / cls.num

        return avg


# 班级总人数
ret = Student.get_stu_num()
print('班级总人数为：', ret)

# 创建3个学生，并打印3个学生的基本信息
s1 = Student('mike', 59)
s2 = Student('yoyo', 88)
s3 = Student('rock', 98)
print(s1)
print(s2)
print(s3)

# 班级总人数
ret = Student.get_stu_num()
print('班级总人数为：', ret)

# 班级总分
ret = Student.get_total_score()
print('班级总分为：', ret)

# 班级平均分
ret = Student.get_avg_socre()
print('班级平均分为：%.2f' % ret)
~~~



**题目2（代码题）**

- 定义一个Animal类(动物类)，拥有

  ​	公有类属性name"动物大家族"

  ​	私有类属性leg"四条腿"

  定义类Cat()，继承自Animal。

  初始化名字为波斯猫

  ​	定义方法play，打印“xxx在玩耍” xxx表示名字

  ​	增加静态方法run，打印“动物们跑起来了”

  ​	增加类方法eat，打印“xxx在吃饭”

  打印cat对象的name

##### 训练提示

* 子类继承父类时是否继承私有属性？
* 当实例的属性名和类属性名相同时，实例对象调用时使用的是哪一个？
* 如何创静态方法？
* 如何创建类方法？

**参考答案**

~~~python
class Animal(object):
    name = "动物大家族"
    __leg = "四条腿"

class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def play(self):
        print("%s在玩耍"%self.name)

    @classmethod
    def eat(cls):
        print("%s在吃饭"%cls.name)

    @staticmethod
    def run():
        print("动物们跑起来了")

c = Cat("波斯猫")
c.play()
c.eat()
print(c.name)
~~~



**题目2（代码题）**

* 自定义一个异常类，判断年龄大小，如果小于0或者大于110，那么抛出自定义异常

**训练提示**

* 自定义异常继承Exception
* 手动抛出异常raise


**参考答案**

~~~python
class AgeInputException(Exception):
    '''自定义的异常类'''
    def __init__(self, age):
        #super().__init__()
        self.age = age

def main():
    try:
        s = int(input('请输入年龄 --> '))
        if s < 0 or s > 110:
            # raise引发一个你定义的异常
            raise AgeInputException(s)
    except AgeInputException as result:#result这个变量被绑定到了错误的实例
        print('ShortInputException: 输入的年龄是 %d'% (result.age))
    else:
        print('年龄没有问题。')

main()
~~~



**题目4（代码题）**

编写代码，提示用户输入文件名， 如果文件存在就打印文件内容，如果文件不存在，捕获异常。

**训练提示**

* 捕获异常try

**参考答案**

~~~python
# 输入目标文件
target_file = input("请输入要打开的文件:")

try:
    f = open(target_file, "r")
    content = f.read()
    print(content)
    f.close()
except Exception as e:
    print(e)
~~~



## 拓展提高

**题目4（代码题）**

创建一个动物的基类,其中有一个run方法

创建一个Cat类继承于动物类，具有私有属性__name = "波斯猫"

创建一个Dog类继承于动物类,具有私有属性__name = "京巴狗"

Cat类中不仅有run方法还有eat方法

Dog类中方法同上

创建一个letRun函数，可以接收动物及其子类对象，并调用run方法 class Cat(Animal):

编写测试代码以验证功能正常

**训练提示**

* 定义一个函数，接收一个类的对象
* 创建出的对象传入到方法中
* 在方法中调用对应的方法

**运行结果：**

~~~
跑起来
波斯猫在跑
波斯猫在吃
京巴狗在跑
京巴狗在吃
~~~

**参考答案**

~~~python
# 1.创建一个动物的基类,其中有一个run方法
class Animal(object):
    def run(self):
        print('跑起来')
        
# 2.创建一个Cat类继承于动物类
class Cat(Animal):
    # 4.Cat类中不仅有run方法还有eat方法
    def __init__(self):
        self.__name = "波斯猫"

    def run(self):
        print('%s在跑'%self.__name)

    def eat(self):
        print('%s在吃'%self.__name)

# 3.创建一个Dog类继承于动物类
class Dog(Animal):
	#5.方法同上
    def __init__(self):
        self.__name = "京巴狗"

    def run(self):
        print('%s在跑'%self.__name)

    def eat(self):
        print('%s在吃'%self.__name)

# 6.创建一个letRun函数，可以接收动物及其子类对象，并调用run方法 class Cat(Animal):
def letRun(animal):
    animal.run()
    
# 7.编写测试代码以验证功能正常
# 动物测试
animal = Animal()
letRun(animal)

# 猫测试
cat = Cat()
letRun(cat)
cat.eat()

# 狗测试
dog = Dog()
letRun(dog)
dog.eat()
~~~



## 自主预习

**题干**

将学生管理系统修改为面向对象版

**参考答案**

~~~python
import os

class StudetClass(object):
    def __init__(self):
        self.student_list = []  # list()
        print("全局变量:", id(self.student_list))

    # 显示功能菜单的函数
    def show_menu(self):
        print("-----学生管理系统v1.0-----")
        print("1. 添加学生")
        print("2. 删除学生")
        print("3. 修改学生信息")
        print("4. 查询学生信息")
        print("5. 显示所有学生信息")
        print("6. 退出")


    # 添加学生
    def add_student(self):
        name = input("请输入学生的姓名:")
        age = input("请输入学生的年龄:")
        sex = input("请输入学生的性别:")

        # 定义学生字典类型的变量
        student_dict = {} # dict()
        # 把学生的信息使用字典进行存储
        student_dict["name"] = name
        student_dict["age"] = age
        student_dict["sex"] = sex

        # 把学生信息添加到学生列表中
        self.student_list.append(student_dict)


    # 显示所有学生信息
    def show_all_student(self):
        for index, student_dict in enumerate(self.student_list):
            # 学号和下标的关系
            student_no = index + 1

            print("学号:%d 姓名:%s 年龄:%s 性别:%s" % (student_no, student_dict["name"],
                                               student_dict["age"], student_dict["sex"]))


    # 删除学生信息
    def remove_student(self):
        student_no = int(input("请输入要删除学生的学号:"))
        # 获取学生字典信息的下标
        index = student_no - 1
        if index >= 0 and index < len(self.student_list):
            # 根据下标删除学生信息
            del self.student_list[index]
        else:
            print("请输入正确的学号")

    # 修改学生信息
    def modify_student(self):
        student_no = int(input("请输入要修改学生的学号:"))
        # 根据学号计算下标
        index = student_no - 1

        if index >= 0 and index < len(self.student_list):
            # 根据下标获取学生字典信息
            student_dict = self.student_list[index]

            name = input("请输入您修改后的名字:")
            age = input("请输入您修改后的年龄:")
            sex = input("请输入您修改后的性别:")

            student_dict["name"] = name
            student_dict["age"] = age
            student_dict["sex"] = sex
        else:
            print("请输入正确的学号")


    # 查询学生
    def search_student(self):
        name = input("请输入要查询的学生姓名:")

        # 遍历学生列表信息
        for index, student_dict in enumerate(self.student_list):
            # pass # 空实现
            if student_dict["name"] == name:
                student_no = index + 1
                # 说明找到了这个学生
                print("学号:%d 姓名:%s 年龄:%s 性别:%s" % (student_no, student_dict["name"],
                                                   student_dict["age"], student_dict["sex"]))
                break
        else:
            print("对不起，没有找到这个学生")


    # 保存学生列表数据到文件中
    def save_data(self):
        file = open("student_list.data", "w", encoding="utf-8")
        # 把列表转成字符串
        student_list_str = str(self.student_list)
        # 把列表数据写入到文件中
        file.write(student_list_str)
        file.close()


    # 加载文件中的数据
    def load_data(self):
        result = os.path.exists("Test")
        print(result)
        # 判断文件或者文件夹是否存在
        if os.path.exists("student_list.data"):
            file = open("student_list.data", "r", encoding="utf-8")

            # 读取文件中的数据
            file_content = file.read()
            new_student_list = eval(file_content)
            print(new_student_list, type(new_student_list))
            # global student_list
            # student_list = new_student_list

            self.student_list.extend(new_student_list)
            print("全局变量:", id(self.student_list))

            file.close()

    # 程序启动的函数
    def run(self):

        # 加载文件中的数据
        self.load_data()

        while True:
            # 显示功能菜单
            self.show_menu()
            # 接收用户的指令
            menu_option = input("请输入您需要的功能选项:")

            if menu_option == "1":
                print("添加学生")
                self.add_student()
            elif menu_option == "2":
                print("删除学生")
                self.remove_student()
            elif menu_option == "3":
                print("修改学生信息")
                self.modify_student()
            elif menu_option == "4":
                print("查询学生信息")
                self.search_student()
            elif menu_option == "5":
                print("显示所有学生信息")
                self.show_all_student()
            elif menu_option == "6":
                # 保存数据到文件
                self.save_data()
                print("退出")
                break

# 执行程序启动的函数
s = StudetClass()
s.run()
~~~





-----