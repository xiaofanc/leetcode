from random import random
from heapq import heapify, heappop, heappush
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
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for i, node in enumerate(lists):
            if node != None:
                heappush(heap, (node.val, random(), node))
                # random() prevent comparison between nodes
                # use list as binary search tree
        curr = prehead = ListNode(0)
        while heap:
            val, _, node = heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            node = node.next
            if node: 
                heappush(heap,(node.val, random(), node))
        return prehead.next

if __name__ == '__main__':
    s = Solution()
    l1 = ListNode.from_list([1,4,5])
    l2 = ListNode.from_list([1,3,4])
    l3 = ListNode.from_list([2,6])
    print(s.mergeKLists([l1,l2,l3]))                
        