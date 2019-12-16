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
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        A = [head]
        # print(A[-1], A[-1].next)
        # [1,2,3,4,5], [2,3,4,5], [3,4,5], [4,5], [5]
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A) / 2]
    
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

s=Solution()
l=ListNode.from_list([1,2,3,4,5,6,7])
print(l)
print(s.middleNode(l))

