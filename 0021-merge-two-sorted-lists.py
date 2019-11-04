class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    def mergeTwoLists0(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = prehead = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1 # = ListNode(l1.val)
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 is not None else l2
        return prehead.next      
"""   
# iteration
class Solution:
	def mergeTwoListsit(self, l1, l2):
		prehead = ListNode(-1)
		prev = prehead
		while l1 and l2:
		    if l1.val <= l2.val:
				prev.next = l1
				l1 = l1.next
		    else:
		        prev.next = l2
		        l2 = l2.next
		    prev = prev.next

		prev.next = l1 if l1 is not None else l2
		return prehead.next
"""

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

s=Solution()
#print(s.mergeTwoLists(l1,l2))
print(s.mergeTwoLists1(l1,l2))
#print(s.mergeTwoListsit(l1,l2))
