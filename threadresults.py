# '''
# Process:
# The process is a program (set of instructions) in execution
# Process cannot share the memory


# Thread:
# Thread is light-weight processes
# Threads can be used to perform complicated tasks in the background without interrupting the main program.
# Threads can Share the memory






# run():is the entry point for a thread.

# start():method starts a thread by calling the run method.

# join([time]):waits for threads to terminate.

# isAlive():method checks whether a thread is still executing.

# getName():method returns the name of a thread.

# '''


# import threading
# from threading import *
# from time import sleep 

# class First_thread(Thread):
#     def run(self):
#         for i in range(10):
#             print("First Thread:",i)
#             sleep(4)

# class Second_thread(Thread):
#     def run(self):
#         for i in range(10):
#             print("Second Thread:",i)
#             sleep(4)

# class Third_thread(Thread):
#     def run(self):
#         for i in range(10):
#             print("Third Thread:",i)
#             sleep(4)

# class Fourth_thread(Thread):
#     def run(self):
#         for i in range(10):
#             print("Fourth Thread:",i)
#             sleep(4)

# t1=First_thread()
# t2=Second_thread()
# t3=Third_thread()
# t4=Fourth_thread()
# t1.start()
# print(t1.is_alive())
# t1.join()
# print(t1.is_alive())
# sleep(1)
# t2.start()
# sleep(1)
# t3.start()
# sleep(1)
# t4.start()
# sleep(1)

















































import threading
print(threading.current_thread().getName())


