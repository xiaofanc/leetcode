class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.val = 0
        self.prev = None
        self.next = None

# hash + doubly linkedlist
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node(self, node):
        # add node right after head
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
        
    def _remove_node(self, node):
        # remove an existing node from list
        prev = node.prev
        new = node.next
        
        new.prev = prev
        prev.next = new
    
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res
        
    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        self._move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)
        if node:
            node.val = value
            self._move_to_head(node)
        else:
            newNode = DLinkedNode()
            newNode.key = key
            newNode.val = value
            self.cache[key] = newNode
            self._add_node(newNode)
            self.size += 1
            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
            
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)