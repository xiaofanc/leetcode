# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        f = odd = head
        s = even = head.next
        while f and s and s.next:
            f.next = s.next
            s.next = s.next.next
            f = f.next
            s = s.next
        f.next = even
        return head
        
