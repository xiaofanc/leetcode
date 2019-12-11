from collections import deque
class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._msg_set = set()
        self._msg_queue = deque()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        while self._msg_queue:
            msg, ts = self._msg_queue[0]
            if timestamp - ts >= 10:      # sliding window
                self._msg_queue.popleft()
                self._msg_set.remove(msg) # expired msg
            else:
                break
        
        if message not in self._msg_set:
            self._msg_queue.append((message, timestamp))
            self._msg_set.add(message)
            return True
        else:
            return False


class Logger:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._msg_dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self._msg_dict:
            self._msg_dict[message] = timestamp
            return True
        
        if timestamp - self._msg_dict[message] >= 10:
            self._msg_dict[message] = timestamp
            return True
        else:
            return False



# Your Logger object will be instantiated and called as such:
logger = Logger()

#logging string "foo" at timestamp 1
print(logger.shouldPrintMessage(1, "foo")) #returns true; 

#logging string "bar" at timestamp 2
print(logger.shouldPrintMessage(2,"bar")) #returns true;

#logging string "foo" at timestamp 3
print(logger.shouldPrintMessage(3,"foo")) #returns false;

#logging string "bar" at timestamp 8
print(logger.shouldPrintMessage(8,"bar")) #returns false;

#logging string "foo" at timestamp 10
print(logger.shouldPrintMessage(10,"foo")) #returns false;

#logging string "foo" at timestamp 11
print(logger.shouldPrintMessage(11,"foo")) #returns true;