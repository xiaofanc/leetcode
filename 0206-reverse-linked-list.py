# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Time: O(N), Space = O(1)
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr is not None:
            nextnode = curr.next
            curr.next = prev
            prev, curr = curr, nextnode
        return prev

    # Time = space = O(N)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        newhead = head
        if head.next:
            newhead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newhead
""" 
recursion:
def reverseListr(self,head): 
    if not head or nor head.next:
        return head
    p = self.reverseListr(head.next)
    head.next.next = head
    head.next = None
    return p
"""     

s=Solution()

print(s.reverseList())    
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL   



