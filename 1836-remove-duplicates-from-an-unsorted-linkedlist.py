# Definition for singly-linked list.
from collections import defaultdict

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        return '%s->%s' % (self.val, self.next or '')

class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        times = defaultdict(int)
        cur = head
        while cur:
            times[cur.val] += 1
            cur = cur.next
        
        prev = dummy = ListNode(0)
        dummy.next = head
        while head:
            if times[head.val] > 1:
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
            
        return dummy.next

if __name__ == '__main__':
    s = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(2)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    print(s.deleteDuplicatesUnsorted(n1)) # [1,3]


