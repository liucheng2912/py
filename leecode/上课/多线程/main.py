import threading
from time import sleep,ctime
import logging
import _thread
logging.basicConfig(level=logging.INFO)

#1
#2
# def loop0():
#     logging.info("start loop0 at" + ctime())
#     sleep(4)
#     logging.info("end loop0 at" + ctime())
#
# def loop1():
#     logging.info("start loop1 at" + ctime())
#     sleep(2)
#     logging.info("end loop1 at" + ctime())

# 1
# def main():
#     logging.info("start all at "+ ctime())
#     loop0()
#     loop1()
#     logging.info("end all at "+ ctime())
# # loop1会等待loop0完成才运行

#2
# def main():
#      logging.info("start all at "+ ctime())
#      _thread.start_new_thread(loop0,())
#      _thread.start_new_thread(loop1,())
#      sleep(6)
#      # 不加sleep6的话会导致主线程运行完毕 直接关闭线程 loop0和loop1就不能运行 _thread的一个缺点
#      logging.info("end all at "+ ctime())

#3 _thread
# loops=[2,4] #传入的是时间
# def loop(nloop,nsec,lock):
#     logging.info("start loop" + str(nloop) +" at "+ctime())
#     sleep(nsec)
#     logging.info("end loop"  + str(nloop) + " at "+ctime())
#     lock.release()#_thread自带的解锁
#
#3
# def main():
#     logging.info("start all at " + ctime())
#     locks=[]
#     nloops= range(len(loops))#线程名字 0 1
#     for i in nloops: #有几个线程上几个锁
#         lock=_thread.allocate_lock()#声明一个锁
#         lock.acquire()#上锁
#         locks.append(lock)
#     for i in nloops:
#         _thread.start_new_thread(loop,(i,loops[i],locks[i]))
#     for i in nloops:
#         while locks[i].locked():pass  #locked自带的判断，在上锁的时候，返回true，进入死循环，没有上锁的应用时，返回false，结束死循环
#
#     # 不加sleep6的话会导致主线程运行完毕 直接关闭线程 loop0和loop1就不能运行 _thread的一个缺点
#     logging.info("end all at " + ctime())

# 4 threading 自带锁操作
#5
loops=[2,4] #传入的是时间
def loop(nloop,nsec):
    logging.info("start loop" + str(nloop) +" at "+ctime())
    sleep(nsec)
    logging.info("end loop"  + str(nloop) + " at "+ctime())


#4
# def main():
#     logging.info("start all at " + ctime())
#     threads=[]
#     nloops= range(len(loops))#线程名字 0 1
#     for i in nloops:
#         t = threading.Thread(target=loop,args=(i,loops[i]))#声明Thread不会立即执行，需要调用start方法
#         threads.append(t)
#     for i in nloops:
#         threads[i].start()
#     for i in nloops:
#         threads[i].join() #若是thread0没有执行完 阻塞在这里
#
#     # 不加sleep6的话会导致主线程运行完毕 直接关闭线程 loop0和loop1就不能运行 _thread的一个缺点
#     logging.info("end all at " + ctime())


# 继承Thread类 重写方法
class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func=func
        self.args=args
        self.name=name
    def run(self): #重写run方法
        self.func(*self.args)
#5
def main():
    logging.info("start all at " + ctime())
    threads=[]
    nloops= range(len(loops))#线程名字 0 1
    for i in nloops:
        t = MyThread(loop,(i,loops[i]),loop.__name__)#声明Thread不会立即执行，需要调用start方法
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join() #若是thread0没有执行完 阻塞在这里

    # 不加sleep6的话会导致主线程运行完毕 直接关闭线程 loop0和loop1就不能运行 _thread的一个缺点
    logging.info("end all at " + ctime())

if __name__ == '__main__':
   main()
