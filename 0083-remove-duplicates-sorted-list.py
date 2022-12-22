from typing import List

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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        prev, curr = head, head.next
        while curr:
            if curr.val == prev.val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev, curr = prev.next, curr.next
        return head

    # 26. Remove Duplicates from Sorted Arra
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        prev, curr = head, head.next
        while curr:
            if curr.val != prev.val:
                prev.next = curr
                prev = prev.next
            curr = curr.next
        prev.next = None
        return head

if __name__ == '__main__':
    s = Solution()
    l = ListNode.from_list([1,2,3,4,4,6,7])
    l2 = ListNode.from_list([1,2,3,4,4,4,4])
    print(s.deleteDuplicates(l))
    print(s.deleteDuplicates(l2))
        
            