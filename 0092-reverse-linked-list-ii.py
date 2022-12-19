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

    # recursion
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverseN(head, n):
            # base case
            if n == 1:
                # 记录第n+1个节点，后面要用
                successor = head.next
                return head, successor
            # 以head.next为起点，需要反转前n-1个节点
            newhead, successor = reverseN(head.next, n-1)
            head.next.next = head
            # 让反转后的head节点和n+1连接起来
            head.next = successor
            return newhead, successor
        
        # base case
        if left == 1:
            newhead, _ = reverseN(head, right)
            return newhead
        
        # 对于head.next来说，就是反转区间[m-1, n-1]
        # 前进到反转的起点触发base case
        head.next = self.reverseBetween(head.next, left-1, right-1)
        return head

if __name__ == '__main__':
    s = Solution()
    print(s.reverseBetween([1,2,3,4,5], 2, 4))  # [1,4,3,2,5]




    