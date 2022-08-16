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
    def reverseLinkedList(self, head, k):
        # return k nodes
        prev, cur = None, head
        while k:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
            k -= 1
        # return new head
        return prev
            
            
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return 
        prev = head  # remember the next start position to be reversed
        count = 0    # count numbers
        # see if ther are at least k nodes left in the linked list
        while count < k and prev:
            prev = prev.next
            count += 1
        if count == k:
            # reverse from head to prev previous node
            reversedHead = self.reverseLinkedList(head, k)
            # connect reversed parts
            # The end of the reverseLinkedList is head!
            # assuming that nodes after prev are already reversed
            # prev is the head for the next k groups
            head.next = self.reverseKGroup(prev, k)
            return reversedHead
        # if count < k
        return head
            
if __name__ == '__main__':
    s = Solution()
    l1=ListNode.from_list([1,2,3,4,5])
    print(s.reverseKGroup(l1, 3))
        
            
            