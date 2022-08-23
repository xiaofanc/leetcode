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
    def isPalindrome1(self, head: ListNode) -> bool:
        # reverse the first part
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            print('line 32:', rev, slow)
            rev, rev.next, slow = slow, rev, slow.next
            print('line 34:', slow, rev)
        #print(slow, rev)
        if fast: # linked list has odd numbers
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev

    def isPalindrome0(self, head: ListNode) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]

s=Solution()
l=ListNode.from_list([1,2,3,4,5,6,7])
print(l)
print(s.isPalindrome1(l))