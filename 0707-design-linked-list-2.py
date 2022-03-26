class ListNode:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt
    
    def __str__(self):
        return '%s->%s' % (self.val, self.next or '')

class MyLinkedList:

    def __init__(self):
        self._prehead = ListNode(0)
        self._count = 0

    def get(self, index: int) -> int:
        if 0 <= index < self._count:
            node = self._prehead
            for i in range(index+1):
                node = node.next
            # print('get', node.val)
            return node.val
        return -1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self._count, val)
        # print('add at tail', self._prehead)
        # print('self._count', self._count)

    def addAtIndex(self, index: int, val: int) -> None:
        if 0 <= index <= self._count:
            prev, curr = None, self._prehead
            for i in range(index+1):
                prev, curr = curr, curr.next
            newnode = ListNode(val)
            prev.next, newnode.next = newnode, curr
            self._count += 1
        # print('add at index', self._prehead)

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self._count:
            prev, curr = None, self._prehead
            for i in range(index+1):
                prev, curr = curr, curr.next
            prev.next = curr.next
            self._count -= 1
        # print('delete at index', self._prehead)
        # print('count', self._count)
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)