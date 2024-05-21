from multiprocessing import Process,Queue
from time import sleep


class MyProcess(Process):
    def __init__(self,name,mq):
        Process.__init__(self)
        self.name = name
        self.mq = mq
    def run(self):
        print(f"Process:{self.name} start")
        print(f'get Data:{self.mq.get()}')
        sleep(2)
        self.mq.put(self.name)
        print(f"Process:{self.name} end")
if __name__ == '__main__':
    # 创建进程列表
    p_list = []
    mq = Queue()
    mq.put('1')
    mq.put('2')
    mq.put('3')
    # 循环创建进程
    for i in range(3):
        p = MyProcess('p{}'.format(i),mq)
        p.start()
        p_list.append(p)
    # 等待进程结束
    for t in p_list:
        t.join()
    print(mq.get())
    print(mq.get())
    print(mq.get())