# Definition for singly-linked list.
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
    
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry=0
        cur = prehead = ListNode('')
        while l1 or l2 or carry:
            v1, v2 = 0, 0 
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, vcur = divmod(v1+v2+carry, 10)
            cur.next = ListNode(vcur)
            cur = cur.next
        return prehead.next

if __name__ == '__main__':
    s = Solution()
    l1 = ListNode.from_list([2,4,3])
    l2 = ListNode.from_list([5,6,4,9])
    l3 = ListNode.from_list([1])
    l4 = ListNode.from_list([9,9,9])
    print(s.addTwoNumbers(l1,l2))
    print(s.addTwoNumbers(l3,l4))

    