"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        frontier = [root]
        while frontier:
            for i in range(len(frontier)-1):
                frontier[i].next = frontier[i+1]
            frontier = [n for f in frontier for n in (f.left, f.right) if n]
        return root

    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        if root.left: 
            root.left.next = root.right
        if root.right:     # 2 conditions
            if root.next:
                root.right.next = root.next.left
            else:
                root.right.next = None
        self.connect(root.left)
        self.connect(root.right)
        return root

if __name__ == '__main__':
    s = Solution()
    print(s.connect([1,2,3,4,5,6,7]))