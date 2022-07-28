import threading

class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.capacity = capacity
        
        self.pushing = threading.Semaphore(capacity)
        # ensure that it doesn't dequeue anything when there's nothing in the queue in the beginning
        self.pulling = threading.Semaphore(0)
        self.editing = threading.Lock()
      
        self.queue = collections.deque()

    def enqueue(self, element: int) -> None:
        self.pushing.acquire()
        self.editing.acquire()

        self.queue.append(element)

        self.editing.release()
        # 'self.pulling.release()' would then allow dequeue to dequeue something from the queue.
        self.pulling.release() 

    def dequeue(self) -> int:
        self.pulling.acquire()
        self.editing.acquire()
        
        res = self.queue.popleft()
        
        self.editing.release()
        self.pushing.release()
        return res

    def size(self) -> int:
        return len(self.queue)

["BoundedBlockingQueue","dequeue","dequeue","dequeue","enqueue","enqueue","enqueue"]
[[3],[],[],[],[1],[0],[2]]

        
