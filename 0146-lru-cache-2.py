class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        # map key to Node
        self.cache = dict()
        self.cap = capacity
        self.size = 0

    def _move_from_list(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
    
    def _add_to_end(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._move_from_list(node)
            self._add_to_end(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._move_from_list(node)
            self.size -= 1

        newnode = Node(key, value)
        self._add_to_end(newnode)
        self.cache[key] = newnode
        self.size += 1
        
        if self.size > self.cap:
            first = self.head.next
            self._move_from_list(first)
            self.size -= 1
            # do not forget to pop from cache !!!!!!!!!!!!!!!!!!!!!
            self.cache.pop(first.key)
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



