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
    def hasCycle0(self, head):
        if not head:
            return False
        slow = head
        fast = head.next
        while slow is not fast: # return True when slow is not fast
            if slow is None or fast is None or fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
        return True
    
    def hasCycle1(self, head):
        if not head:
            return False
        slow = head
        fast = head.next
        while slow and fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

s=Solution()
l=ListNode.from_list([1,2,3,4,5,6,7])
print(l)
print(s.hasCycle0(l))  
        
            