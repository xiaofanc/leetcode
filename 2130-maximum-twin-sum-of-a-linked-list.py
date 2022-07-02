"""
The number of nodes in the list is an even integer.

               0 1 2 3
Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        l, r = 0, len(lst)-1
        res = float("-inf")
        while l < r:
            res = max(res, lst[l]+lst[r])
            l += 1
            r -= 1
        return res

    # reverse the second part of the linked list
    def pairSum(self, head: Optional[ListNode]) -> int:
        res = float("-inf")
        s = f = head
        while f and f.next:
            f = f.next.next
            s = s.next
        # now s is the end of the second part
        # reverse the second part
        cur, prev = s, None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev, cur = cur, tmp
        # now prev is the head of the second part
        while prev and head:
            res = max(res, prev.val + head.val)
            prev, head = prev.next, head.next
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.pairSum([5,4,2,1]))  # 6




