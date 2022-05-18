import queue
import time
from threading import Thread, Lock

UUID = 0
BUFFER = queue.Queue(maxsize=10)
MUTEX = Lock()

class Producer(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        global UUID
        while True:
            MUTEX.acquire()
            if BUFFER.full():
                print("Buffer is full, producer is waiting")
                MUTEX.release()
            else:
                UUID += 1
                BUFFER.put(UUID)
                print("Producer", self.name, "produced:", UUID)
                MUTEX.release()
            time.sleep(1)

class Consumer(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        while True:
            MUTEX.acquire()
            if BUFFER.empty():
                print("Buffer is empty")
                MUTEX.release()
                time.sleep(1)
                continue
            print("Consumer", self.name, "Consumed:", BUFFER.get())
            MUTEX.release()
            time.sleep(1)

for i in range(20):
    t = Producer(i)
    t.start()

for i in range(2):
    t = Consumer(i)
    t.start()
