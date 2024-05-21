#coding=utf-8
from queue import Queue
from threading import Thread
from time import sleep

def producer():
    num = 1
    while True:
        if queue.qsize()<5:
            print(f"生产{num}号，大馒头")
            queue.put(f"大馒头：{num}号")
            num +=1
        else:
            print("馒头框满了，等待来人消费啊！")
        sleep(1)

def consumer():
    while True:
        print(f"获取馒头：{queue.get()}")
        sleep(1)

if __name__ == '__main__':
    queue = Queue()
    t1 = Thread(target=producer)
    t2 = Thread(target=consumer)
    t1.start()
    t2.start()