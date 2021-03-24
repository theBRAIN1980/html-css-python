import time
import threading

class MyThread(threading.Thread):
    def run(self):
        global numbers
        for i in range(10):
            print(i)
            time.sleep(0.5)

mt1 = MyThread()
mt2 = MyThread()
mt1.start()

print()
mt2.start()
mt1.join()
