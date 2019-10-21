# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre=dummy=ListNode(0)
        pre.next=head
        while pre.next and pre.next.next:
            n1 = pre.next
            n2 = n1.next
            #pre.next,n2.next,n1.next=n2,n1,n2.next
            next_node = n2.next
            pre.next = n2
            n2.next=n1
            n1.next=next_node
            pre = n1
        return dummy.next
            

Given 1->2->3->4, you should return 2->1->4->3