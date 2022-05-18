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
            while not BUFFER.full():
                UUID += 1
                BUFFER.put(UUID)
                print("Producer {}: Produced {}".format(self.name, UUID))
                time.sleep(0.1)
            MUTEX.release()	# release the lock
            time.sleep(0.5)

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
            print("Consumer {} consumed: {}".format(self.name, BUFFER.get()))
            MUTEX.release()
            time.sleep(1)

for i in range(2):
    t = Producer(i)
    t.start()

for i in range(10):
    t = Consumer(i)
    t.start()
