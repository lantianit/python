# day09 每日练习题

## 当天知识点回顾

* 了解对象和类的关系

  * 对象是对客观事物的抽象，类是对对象的抽象。类是一种抽象的数据类型。 它们的关系是，对象是类的实例，类是对象的模板。

* 类的构成

  * 类名、属性、方法

* 掌握如何创建类

  ~~~python
  class 类名(object)：
  	pass
  ~~~

  

* 掌握使用类创建对象

  ~~~python
  变量名 = 类名()
  ~~~

* 掌握给对象添加获取属性

  ~~~python
  # 方法一：
  对象名.属性名 = 值
  
  # 方法二：
  __init__(self)魔法方法
  ~~~

  

* 魔法方法
  *  \__init__   初始化属性
  * \__str__   打印对象时掉用
  *  \__del__ 删除对象时调用    
  
* 知道什么是单继承

  * 一个子类只有一个父类

* 知道什么是多继承

  * 一个子类可以有多个父类

* super的作用是什么

  * 使用super() 可以逐一调用所有的父类方法，并且只执行一次。调用顺序遵循 **mro** 类属性的顺序。

    **注意：如果继承了多个父类，且父类都有同名方法，则默认只执行第一个父类的(同名方法只执行一次，目前super()不支持执行多个父类的同名方法)**

* 私有属性和私有方法

  * 在属性名和方法名 前面 加上两个下划线 __
  * 类的私有属性 和 私有方法，都不能通过对象直接访问，但是可以在本类内部访问；
  * 类的私有属性 和 私有方法，都不会被子类继承，子类也无法访问；
  * 私有属性 和 私有方法 往往用来处理类的内部事情，不通过对象处理，起到安全作用。

## 

## 每日练习

**题目1（代码题）**

- 题干：定义一个star类(明星类)， 通过明星类创建一个zhou_xing_chi对象。

##### 训练提示

1. 定义一个类
2. 创建一个对象

**参考答案**

~~~python
class Star():
    pass

zhou_xing_chi = Star()
~~~



**题目2（代码题）**

* 题干：定义一个star类(明星类)， 通过明星类创建一个zhou_xing_chi对象，通过对象给对象添加属性 

​	明星姓名= “周星驰”

​	明星的电影 = “功夫”

**训练提示**

* 添加属性方法1

  对象名.属性名 = 值

* 添加属性方法1

  在init方法中给对象添加属性

**参考答案**

~~~python
#  创建类
class Star():
    # 初始空属性
    def __init__(self):
        self.name = None
        self.movie = None
# 设置属性
zhou_xing_chi = Star()
zhou_xing_chi.name = "周星驰"
zhou_xing_chi.movie = "功夫"

# 打印属性
print(zhou_xing_chi.name)
print(zhou_xing_chi.movie)
~~~



**题目3（代码题）**

定义一个star类(明星类)， 通过明星类创建一个zhou_xing_chi对象

使用\__init__方法给对象添加属性 

定义方法playing()，打印“xxx出演了yyy，非常好看”

**训练提示**

* 使用self保存私有属性
* 调用方法打印结果

**运行结果：**

~~~
周星驰出演了功夫，非常好看
~~~

**参考答案**

~~~python
class Star():
    def __init__(self,name,movie):
        self.name = name
        # 定义私有属性
        self.__movie = movie
    
    def playing(self):
        print("%s出演了%s，非常好看" % (self.name,self.__movie) )

zhou_xing_chi = Star("周星驰","功夫")

zhou_xing_chi.playing()
~~~



**题目4（代码题）**

定义一个star类(明星类)， 通过明星类创建一个zhou_xing_chi对象

使用init方法给对象添加属性 

print输出对象时打印"xxx是我的偶像，我非常喜欢他的电影yyy"

xxx为明星姓名，yyy是电影的名字

**训练提示**

* 使用str方法用来显示信息
* 该方法需要 return 一个数据，并且只有self一个参数，当在类的外部 print(对象) 则打印这个数据

**运行结果：**

~~~
周星驰是我的偶像，我非常喜欢他的电影功夫
~~~

**参考答案**

~~~python
class Star():
    def __init__(self,name,movie):
        self.name = name
        self.movie = movie
    
    # 注意__str__ 要返回一个字符串
    def __str__(self):
        return "%s是我的偶像，我非常喜欢它的电影%s"  % (self.name,self.movie)

zhou_xing_chi = Star("周星驰","功夫")

print(zhou_xing_chi)
~~~



**题目4（代码题）**

定义一个star类(明星类)， 通过明星类创建一个zhou_xing_chi对象

使用init方法给对象添加属性 

删除创建的对象，打印“我不喜欢xxx了”

**训练提示**

* 当删除对象时，python解释器也会默认调用一个方法，这个方法为`__del__()`方法 
* 当有变量保存了一个对象的引用时，此对象的引用计数就会加1； 
* 当使用del() 删除变量指向的对象时，则会减少对象的引用计数。如果对象的引用计数不为1，那么会让这个对象的引用计数减1，当对象的引用计数为0的时候，则对象才会被真正删除（内存被回收）。 

**运行结果：**

~~~
我不喜欢周星驰了
~~~

**参考答案**

~~~python
class Star():
    def __init__(self,name):
        self.name = name
      
    def __del__(self):
        print("我不喜欢%s了" % self.name)
    
zhou_xing_chi = Star("周星驰")

del zhou_xing_chi
~~~





## 拓展提高

 **题目1（代码题）**

a.定义一个Star类(明星类)，包含初始化init方法：

 成员属性：明星姓名

​		    明星的电影

成员方法：playing()

​	打印：“xxx出演了yyy，非常好看”

打印对象时显示“xxx是我的偶像，我非常喜欢他的电影yyy”

删除对象提示“xxx我不再喜欢了”

xxx为明星姓名，yyy是电影的名字

b.键盘循环输入五个Star对象的姓名和电影名。

c.分别调用输入Star对象的playing方法和打印对象

**训练提示**

* 创建类
* init初始化
* str打印对象
* del删除对象
* 使用列表保存创建的类对象

**运行结果：**

~~~python
请输入你喜欢的明星:周星驰
请输入电影名功夫
请输入你喜欢的明星:刘德华
请输入电影名狄仁杰
请输入你喜欢的明星:周润发
请输入电影名赌神
周星驰出演了功夫，非常好看
周星驰是我的偶像，我非常喜欢他的电影功夫
刘德华出演了狄仁杰，非常好看
刘德华是我的偶像，我非常喜欢他的电影狄仁杰
周润发出演了赌神，非常好看
周润发是我的偶像，我非常喜欢他的电影赌神
我不喜欢周星驰了
我不喜欢刘德华了
我不喜欢周润发了
~~~

**参考答案**

~~~python
class Star():
    def __init__(self,name,movie):
        self.name = name
        self.movie = movie
    
    # 注意__str__ 要返回一个字符串
    def __str__(self):
        return "%s是我的偶像，我非常喜欢它的电影%s"  % (self.name,self.movie)
    def playing(self):
        print("%s出演了%s，非常好看" % (self.name,self.movie))
        
    def __del__(self):
        print("%s我不再喜欢了" % self.name)

stars = []

for i in range(5):
    # 接收用户输入的名字跟电影
    name = input("请输入明星名字: ")
    movie = input("请输入电影名字: ")
    # 构造明星对象
    star = Star(name,movie)
    # 添加到明星列表
    stars.append(star)
    
# 打印明星信息
for star in stars:
    star.playing()
    print(star)
    
# del 删除对象
del stars
~~~



 **题目2（代码题）**

- 开发小美和狗玩的案例

  1.定义Dog类，初始化属性为name（需要在创建对象时传入init方法中）。

  2.在Dog类中定义game方法，输出“name + 开始奔奔跳跳的玩耍”

  3.创建一个woman类，初始化属性为name，age（需要在创建对象时传入init方法中）。

  4.其中age属性为私有变量。

  5.定义陪狗玩的方法play_with_dog输出主人及狗的名字，并调用狗的game方法。

**训练提示**

* 创建一个Dog类
  * 初始化名字
  * 定义game方法
* 创建一个Woman类
  * 初始化name
  * 定义方法play_with_dog
* 注意：
  * 在play_with_dog方法中传入的是dog对象

##### 参考答案

```python
class Dog(object):
    def __init__(self,name):
        self.name = name
    
    def game(self):
        print("%s开始奔奔跳跳的玩耍" % self.name)
    
class Woman(object):
    def __init__(self,name,age):
        self.name = name
        self.__age = age
        
    def play_with_dog(self,dog):
        print("%s 陪着 %s 玩耍了" % (self.name,dog.name))
        dog.game()
        
xiaoli = Woman("小丽", 30)
xiaohei = Dog("小黑")

xiaoli.play_with_dog(xiaohei)
```



**题干**

创建一个动物的基类,其中有一个run方法

创建一个Cat类继承于动物类，Cat类中不仅有run方法还有eat方法

创建一个BosiCat类继承与Cat类，初始化init方法name为波斯猫

**训练目标**

* 多层继承

**训练提示**

* 多层继承父类

**操作步骤**

* 定义Animal类
* 定义Cat类继承Animal类
* 定义BosiCat类继承Cat类

**参考答案**

~~~python
class Animal(object):
    def run(self):
        print("咻的一下，跑远了")
        
        
class Cat(Animal):
    def eat(self,food):
        print("%s 肚子饿了, 吃了%s" % (self.name,food))
        

class BosiCat(Cat):
    def __init__(self):
        self.name = "波斯猫"
        
        
        
bc = BosiCat()
bc.run()
bc.eat("小鱼")
~~~

