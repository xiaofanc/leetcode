from collections import OrderedDict
# orderdict 
class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1 
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)
        

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        # add to the end automatically
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)


if __name__ == '__main__':
    cache = LRUCache(2)

    cache.put(1, 1);
    cache.put(2, 2);
    print(cache.get(1)); # returns 1
    cache.put(3, 3);     # evicts key 2
    print(cache.get(2)); # returns -1 (not found)
    cache.put(4, 4);     # evicts key 1
    print(cache.get(1)); # returns -1 (not found)
    print(cache.get(3)); # returns 3
    print(cache.get(4)); # returns 4