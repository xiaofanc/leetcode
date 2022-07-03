# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        M = [[-1]*n for i in range(m)]
        top, bottom, left, right = 0, m-1, 0, n-1
        if m == 1 and n == 1:
            M[0][0] = head.val
            return M
        while top <= bottom and left <= right:
            if not head:
                return M
            for j in range(left, right):
                M[top][j] = head.val
                head = head.next
                if not head: return M
            for i in range(top, bottom):
                M[i][right] = head.val
                head = head.next
                if not head: return M
            for j in range(right, left, -1):
                M[bottom][j] = head.val
                head = head.next
                if not head: return M
            for i in range(bottom, top, -1):
                M[i][left] = head.val
                head = head.next
                if not head: return M
            top += 1
            bottom -= 1
            left += 1
            right -= 1
            
        
