import threading

class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.capacity = capacity
        
        self.pushing = threading.Semaphore(capacity)
        # ensure that it doesn't dequeue anything when there's nothing in the queue in the beginning
        self.pulling = threading.Semaphore(0)

        # separate "editing" lock shared by both the enqueue and dequeue operators, which would prevent them from modifying the queue concurrently.
        self.editing = threading.Lock()
      
        # Can we use list here instead of deque, since deque is already thread safe?
        self.queue = collections.deque()

    def enqueue(self, element: int) -> None:
        self.pushing.acquire()
        self.editing.acquire()

        self.queue.append(element)

        self.editing.release()
        # allow dequeue
        self.pulling.release() 

    def dequeue(self) -> int:
        self.pulling.acquire()
        self.editing.acquire()
        
        res = self.queue.popleft()
        
        self.editing.release()
        # allow enqueue
        self.pushing.release()
        return res

    def size(self) -> int:
        return len(self.queue)


# solution 2: Lock()
# When the state is unlocked, acquire() changes the state to locked and returns immediately. When the state is locked, acquire() blocks until a call to release() in another thread changes it to unlocked, then the acquire() call resets it to locked and returns.
from threading import Lock
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.en, self.de = Lock(), Lock()
        self.lst = []
        self.capacity = capacity
        self.de.acquire() # lock dequeue initially
        self.edit = Lock() # avoid enqueue and dequeue modifying the queue concurrently.

    def enqueue(self, element: int) -> None:
        # If the queue is full, the calling thread is blocked until the queue is no longer full.
        self.en.acquire()
        self.edit.acquire()
        self.lst.append(element)
        if self.size() < self.capacity:
            self.en.release()
        if self.de.locked():
            self.de.release()
        self.edit.release()

    def dequeue(self) -> int:
        # If the queue is empty, the calling thread is blocked until the queue is no longer empty.
        self.de.acquire() # block if already locked
        self.edit.acquire()
        val = self.lst.pop(0)
        if self.size() > 0:  # self.size() is a method!
            self.de.release()
        if val and self.en.locked():
            self.en.release()
        self.edit.release()
        return val

    def size(self) -> int:
        return len(self.lst)

        

        
        
