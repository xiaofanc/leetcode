from collections import OrderedDict

class LRUCache():

    def __init__(self, capacity: int):
        self.od = OrderedDict()
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key not in self.od:
            return -1
        self.od.move_to_end(key)
        return self.od[key]
        
    def put(self, key: int, value: int) -> None:
        if key in self.od:
            self.od.move_to_end(key)
        self.od[key] = value
        if len(self.od) > self.capacity:
            self.od.popitem(last=False) # remove the first
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)