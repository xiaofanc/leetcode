# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.pool = []
        cur = head
        self.pos = 0
        while cur:
            self.pool.append(cur.val)
            self.pos += 1
            cur = cur.next
        
    def getRandom(self) -> int:
        idx = random.randint(0, self.pos-1)
        return self.pool[idx]

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()