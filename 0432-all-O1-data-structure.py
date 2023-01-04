"""
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

https://leetcode.com/problems/all-oone-data-structure/solutions/697096/swift-clean-code-diagram-doubly-linked-list-hash-map-hash-set/

Do not forget to remove node if keyset is empty, do it in the end since we need to use cur.prev / cur.next
Do not forget to remove key from cache in dec() since it is possible we will delete it forever
"""
# doubly linked list + hashmap
class Node:
    def __init__(self, val=0):
        # val is the count of str
        # keyset is the set of strs with the same count
        self.val = val
        self.keyset = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        # map key to Node
        self.cache = dict()

    def _insertAfter(self, cur, node):
        nextnode = cur.next
        cur.next = node
        node.prev = cur
        node.next = nextnode
        nextnode.prev = node

    def _remove(self, cur):
        prevnode = cur.prev
        nextnode = cur.next
        prevnode.next = nextnode
        nextnode.prev = prevnode

    def inc(self, key: str) -> None:
        if key not in self.cache:
            cur = self.head
        else:
            cur = self.cache[key]
            cur.keyset.remove(key)

        # add to next node
        if cur.val + 1 != cur.next.val:
            newnode = Node(cur.val+1)
            self._insertAfter(cur, newnode)
        else:
            newnode = cur.next

        newnode.keyset.add(key)
        self.cache[key] = newnode
        # print("self.cache", key, self.cache[key].val)

        # remove node if keyset is empty, do not remove head
        # do not remove cur before if cur.val + 1 != cur.next.val
        if len(cur.keyset) == 0 and cur.val != 0: 
            self._remove(cur)

    def dec(self, key: str) -> None:
        if key not in self.cache:
            return
        
        cur = self.cache[key]
        self.cache.pop(key) # do not forget
        cur.keyset.remove(key)

        # add to prev node
        if cur.val - 1 > 0:
            if cur.val - 1 != cur.prev.val:
                newnode = Node(cur.val-1)
                self._insertAfter(cur.prev, newnode)
            else:
                newnode = cur.prev
            newnode.keyset.add(key)
            self.cache[key] = newnode

        # remove node if cur.keyset is empty, cur will not be head
        if len(cur.keyset) == 0: 
            self._remove(cur)

    def getMaxKey(self) -> str:
        # print("get max key from self.cache, hello", self.tail.prev.keyset)
        if self.tail.prev.val != 0:
            key = self.tail.prev.keyset.pop()
            self.tail.prev.keyset.add(key)
            return key
        else:
            return ""

    def getMinKey(self) -> str:
        # print("get min key from self.cache, hello", self.head.next.keyset)
        if self.head.next.val != 0:
            key = self.head.next.keyset.pop()
            self.head.next.keyset.add(key)
            return key
        else:
            return ""

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()




