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

"""
fast首先走n + 1步 ，为什么是n+1呢，因为只有这样同时移动的时候slow才能指向删除节点的上一个节点.
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointers with n numbers apart
        # when fast pointer reaches the end, the slow pointer points to the previous node of the to-be-deleted node
        # create the dummy head in case head needs to be deleted
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        # advance the fast pointer until the gap is n nodes apart
        # fast needs to go n+1 steps
        for i in range(n+1):
            fast = fast.next
        # fast和slow同时移动，直到fast指向末尾
        while fast:
            fast = fast.next
            slow = slow.next
        #fast 走到结尾后，slow的下一个节点为倒数第N个节点
        slow.next = slow.next.next 
        return dummy.next

if __name__ == '__main__':
    s = Solution()
    l=ListNode.from_list([1,2,3,4,5])
    print(s.removeNthFromEnd(l, 2)) # [1,2,3,5]




