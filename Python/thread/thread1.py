import threading from threading
class FirstThread(Thread):
    def run(self):
        print("Run executed....")
        


t1 = FirstThread()
t2 = FirstThread()
t1.start() 
t2.start()