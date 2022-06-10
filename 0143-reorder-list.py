"""
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

- Reverse the second half linked list (slow and fast pointers)
- need to set the first and second half end point to None
- Merge the first half and the second half linked list
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def mergeTwolist(l1, l2):
            dummy = prev = ListNode(0)
            while l1 and l2:
                tmp = l1.next
                prev.next = l1
                prev = prev.next
                prev.next = l2
                prev = prev.next
                l1, l2 = tmp, l2.next
            prev.next = l1 if l1 else l2
            return dummy.next

        # def mergeTwolist(l1, l2):
        #     while l2:
        #         tmp1, tmp2 = l1.next, l2.next
        #         l1.next = l2
        #         l2.next = tmp1
        #         l1, l2 = tmp1, tmp2
                
        def reverseList(head):
            prev, cur = None, head
            while cur:
                curNext = cur.next
                cur.next = prev
                prev, cur = cur, curNext
            return prev
        
        if not head or not head.next:
            return head
        # find the the end of the first half -> slow
        # set the end of the first part point to None
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # first get the head of the second half
        tmp = slow.next
        slow.next = None 
        # reverse the second half
        head2 = reverseList(tmp)
        merged = mergeTwolist(head, head2)
        return merged
        

# reorderList(1->2->3->4)
# = merge 1->2 & 4->3
# = 1->4->2->3
            
            
        
        

            
            
        
        

            
            
        

