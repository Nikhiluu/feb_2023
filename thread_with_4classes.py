import threading
from threading import *
from time import sleep


class First_thread(Thread):
    def run(self):
        for i in range(10):
            print("First Thread:",i)
            sleep(4)
class Second_thread(Thread):
    def run(self):
        for i in range(10):
            print("Second Thread:",i)
            sleep(4)
class Third_thread(Thread):
    def run(self):
        for i in range(10):
            print("Third Thread:",i)
            sleep(4)
class Fourth_thread(Thread):
    def run(self):
        for i in range(10):
            print("Fourth Thread:",i)
            sleep(4)
t1=First_thread()
t2=Second_thread()
t3=Third_thread()
t4=Fourth_thread()
t1.start()
t1.join()
print(t1.is_alive())
sleep(1)
t2.start()
sleep(1)
t3.start()
sleep(1)
t4.start()
sleep(1)
