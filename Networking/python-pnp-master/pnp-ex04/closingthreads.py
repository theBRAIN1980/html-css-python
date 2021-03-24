import threading, time
import datetime

class MyThread(threading.Thread):
    active = False
    def stop_thread(self):
        self.active = False
    def run(self): 
            self.active = True
            print("I am going to sleep 10 seconds")
            time1 = datetime.datetime.now()
            for i in range(1000):
                time.sleep(0)
                if not self.active:
                    return
            time2 = datetime.datetime.now()
            print(f"It took {time2-time1} s")
mt = MyThread() 
mt.start()  
time.sleep(2)
print("Hey, wake up!")
#mt.stop_thread()

