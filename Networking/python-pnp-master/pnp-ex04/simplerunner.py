import _thread, time
import random

def handler():  
    id = _thread.get_ident()
    time.sleep(random.randint(1,3))
    print(f"Hello from thread: {id}")

for i in range(10):
    id = _thread.start_new_thread(handler, ())
    print(f"Created thread with id: {id}")
    time.sleep(1)




