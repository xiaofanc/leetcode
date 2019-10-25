class ListNode:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

    def __str__(self):
        return '%s->%s' % (self.val, self.next or '')

    def __gt__(self, other):
        return True

    def __lt__(self, other):
        return False

    @classmethod
    def from_list(cls, nums):
        if nums == []: return None
        else: return cls(nums[0], cls.from_list(nums[1:]))

class Solution(object):
    def getIntersectionNode0(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        while not headA and not headB:
            return None
        
        pointerA = headA
        pointerB = headB
        
        while pointerA != pointerB:
            pointerA = headB if pointerA is None else pointerA.next
            pointerB = headA if pointerB is None else pointerB.next
        
        return pointerA
    
    def getIntersectionNode1(self, headA, headB):
        curA, curB, lenA, lenB = headA, headB, 0, 0
        while curA != None:
            lenA += 1; curA = curA.next
        while curB != None:
            lenB += 1; curB = curB.next
        print('44', lenA, lenB)
        curA, curB = headA, headB
        if lenA > lenB:
            for _ in range(lenA - lenB):
                curA = curA.next
        else:
            for _ in range(lenB - lenA):
                curB = curB.next
        while curA != None and curB != None:
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next

        return None

s=Solution()
l1=ListNode.from_list([1,2,3,4,5,6,7])
l2=ListNode.from_list([3,10,2,9,547,5,6,7])

N = ListNode
tail = N(5,N(6,N(7)))
l1 = N(1,N(2,N(3,N(4,tail))))
l2 = N(3, N(10,N(2,N(9,N(547,tail)))))

print(l1)
print(l2)
print(s.getIntersectionNode0(l1, l2))
print(s.getIntersectionNode1(l1, l2))  
