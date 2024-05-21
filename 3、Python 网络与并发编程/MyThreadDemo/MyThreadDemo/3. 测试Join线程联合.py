#encoding=utf-8
from threading import Thread
from time import sleep
def func1(name):
    for i in range(3):
        print(f"thread:{name} :{i}")
        sleep(1)

if __name__ == '__main__':
    print("主线程，start")
    #创建线程
    t1 = Thread(target=func1,args=("t1",))
    t2 = Thread(target=func1,args=("t2",))
    #启动线程
    t1.start()
    t2.start()
    #主线程会等待t1,t2结束后，再往下执行
    t1.join()
    t2.join()
    print("主线程，end")