#encoding=utf-8
from threading import Thread
from time import sleep

class MyThread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name =name
    def run(self):
        for i in range(3):
            print(f"thread:{self.name} :{i}")
            sleep(1)

if __name__ == '__main__':
    print("主线程，start")
    #创建线程(类的方式)
    t1 = MyThread('t1')
    #t1设置为守护线程
    t1.daemon = True
    # t1.setDaemon(True)
    #启动线程
    t1.start()
    print("主线程，end")