age = 18

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age


p1 = Person('xiaoming', 15)

print(p1.__dict__)  # {'name': 'xiaoming', 'age': 15}

p1.__dict__ = {'name': 'xiaohong', 'age': 15}

print(p1.name)