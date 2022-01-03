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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointers with n numbers apart
        # when first pointer reaches the end, the second pointer points to the previous node of the to-be-deleted node
        # create the dummy head in case head needs to be deleted
        dummy = ListNode(0)
        dummy.next = head
        second = first = dummy
        # advance the first pointer until the gap is n nodes apart
        # first needs to go n+1 steps
        for i in range(n+1):
            first = first.next
        while first:
            first = first.next
            second = second.next
        # second pointer points to the node before the to-be-deleted node
        second.next = second.next.next 
        return dummy.next

if __name__ == '__main__':
    s = Solution()
    l=ListNode.from_list([1,2,3,4,5])
    print(s.removeNthFromEnd(l, 2)) # [1,2,3,5]




