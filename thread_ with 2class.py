import threading
from threading import *
from time import sleep 

class First_thread(Thread):
    def run(self):
      for i in range(10):
        print("First Thread:",i)
        

class Second_thread(Thread):
    def run(self):
        for i in range(10):
            print("Second Thread:",i)
            sleep(4)
t1= First_thread()
t2= Second_thread()
t1.start()
t2.start()

