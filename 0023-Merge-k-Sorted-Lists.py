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
    # time: O(nlogk), space: O(k)
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for i, node in enumerate(lists):
            # make sure node is not None !!
            if node != None:
                # add the first node of lists, random() makes tuples comparable 
                # If two elements have the same val, the next tuple items will be compared:
                # random() to make it unique
                heappush(heap, (node.val, random(), node))
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

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        cur = prehead = ListNode(0)
        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = ListNode(val)
            if node.next:
                node = node.next
                # recycling tie-breaker i guarantees uniqueness
                # print(node.val, i)
                heapq.heappush(heap, (node.val, i, node))
            cur = cur.next
        return prehead.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # merge by pairs
        # Time: O(nlogk)
        if not lists or len(lists) == 0:
            return None
            
        while len(lists) > 1:
            mergeLists = []
            for i in range(0, len(lists), 2): # logk
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergeLists.append(self.mergeTwolist(l1, l2))
            lists = mergeLists
        return lists[0]

    def mergeTwolist(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next
                
if __name__ == '__main__':
    s = Solution()
    l1 = ListNode.from_list([1,4,5])
    l2 = ListNode.from_list([1,3,4])
    l3 = ListNode.from_list([2,6])
    l4 = listNode.from_list([])
    print(s.mergeKLists([l1,l2,l3]))                
    print(s.mergeKLists([l4]))  # []
    print(s.mergeKLists([]))  # []



        