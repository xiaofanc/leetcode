# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        cur = head
        lst = []
        while cur:
            lst.append(cur.val)
            cur = cur.next
        
        def buildTree(lst):
            if not lst:
                return None
            mid = len(lst) // 2
            node = TreeNode(lst[mid])
            node.left = buildTree(lst[:mid])
            node.right = buildTree(lst[mid+1:])
            return node
        return buildTree(lst)


class Solution:
    def findMiddle(self, head):
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if prev:
            prev.next = None
        return slow

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        if not head:
            return None
        mid = self.findMiddle(head)
        node = TreeNode(mid.val)

        if head == mid:
            return node

        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node

        
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        if not head:
            return None
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if prev:
            prev.next = None

        node = TreeNode(slow.val)
        # base case:
        if head == slow:
            return node
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(slow.next)
        return node


        
        


        
        
