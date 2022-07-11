# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        if m == n: return head
        # reverse linkedlist[m, n], connect m-1 with n and connect n+1 with m
        # find the prev node before m
        # prev is m-1
        prev = dummy = ListNode(0)
        dummy.next = head
        for i in range(m-1):
            prev = prev.next
        
        # reverse [m, n]
        cur = prev.next  # m
        tail = None
        for i in range(n-m+1):
            curNext = cur.next
            cur.next = tail
            tail, cur = cur, curNext
        
        # now tail is n, cur is n+1
        prev.next.next = cur
        prev.next = tail
        
        return dummy.next
            
if __name__ == '__main__':
    s = Solution()
    print(s.reverseBetween([1,2,3,4,5], 2, 4))  # [1,4,3,2,5]




    