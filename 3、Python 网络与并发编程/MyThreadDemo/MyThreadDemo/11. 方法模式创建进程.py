#coding=utf-8
import os
from multiprocessing import Process
from time import sleep


def fun1(name):
    print(f"当前进程ID:{os.getpid()}")
    print(f"父进程ID：{os.getppid()}")
    print(f"Process:{name},start")
    sleep(3)
    print(f"Process:{name},end")

#windows上多进程实现的bug。如果不加main的限制，就会无限制的创建子进程，从而报错。
if __name__ == '__main__':
    print("当前进程ID:",os.getpid())
    #创建进程
    p1 = Process(target=fun1,args=("p1",))
    p2 = Process(target=fun1, args=("p2",))
    #启动进程
    p1.start()
    p2.start()