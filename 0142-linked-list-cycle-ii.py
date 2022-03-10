"""
Consider the following linked list, where E is the cylce entry and X, the first crossing point of fast and slow.
a: distance from head to cycle entry E
c: distance from E to X
b: cycle length

                  __X__
                 /     \
head_____H______E       \
                \       /
                 \_____/    
First step: find the intersection
2*(a+c) = a+c+nb
   a+c  = nb
   a = nb-c
Second step:
Thus if two pointers start from head and X, 
one reaches E, the other also reaches E

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head  # fast = head.next does not work
        # find the intersection if there is a cycle
        while fast and fast.next: # while slow != fast does not work
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None

        # when fast meet slow, reset fast as head
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast

    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        node = head
        while node:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next
        return None
        
if __name__ == '__main__':
    s = Solution()
    print(s.detectCycle([3,2,0,-4], 1))





    