"""
只有当左右孩子都为空的时候，才说明遍历的最低点了。如果其中一个孩子为空则不是最低点.
Python list implementation is array-based. pop(0) removes the first item from the list and it requires to shift left len(lst) - 1 items to fill the gap.
deque() implementation uses a doubly linked list. No matter how large the deque, deque.popleft() requires a constant (limited above) number of operations.

"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:          # root is None, return 0
            return 0
        children = [root.left, root.right]
        if not any(children): 
        # = if root.left is None and root.right is None
            return 1
        min_depth = float("inf")
        for c in children:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return min_depth + 1
    
    #DFS    
    def minDepth(self, root: TreeNode) -> int:
        if not root:          # root is None, return 0
            return 0
        else:
            stack, mindepth = [(1, root)], float("inf")
        while stack:
            depth, root = stack.pop()
            children = [root.left, root.right]
            if not any(children):
                mindepth = min(depth, mindepth)
            for c in children:
                if c:
                    stack.append((depth+1, c))
        return mindepth

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = deque([(root, 1)])
        while level:
            node, depth = level.popleft()  # O(1), list pop(0) is O(N)
            if not node.left and not node.right:
                return depth
            if node.left:
                level.append((node.left, depth+1))
            if node.right:
                level.append((node.right, depth+1))
        return 0

    #BFS
    def minDepth(self, root: TreeNode) -> int:
        if not root:          # root is None, return 0
            return 0
        else:
            node_deque = deque([(1, root),])
            print(node_deque)
        while node_deque:
            depth, root = node_deque.popleft()
            children = [root.left, root.right]
            if not any(children):
                return depth
            for c in children:
                if c:
                    node_deque.append((depth+1, c))

    # https://leetcode.com/problems/minimum-depth-of-binary-tree/discuss/36094/My-solution-in-python
    def minDepth(self, root):
        if root == None:
            return 0
        if not root.left or not root.right:
            return self.minDepth(root.left)+self.minDepth(root.right)+1
        return min(self.minDepth(root.right),self.minDepth(root.left))+1

    def minDepth(self, root):
        if not root:
            return 0
        if not root.left or not root.right:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
    
    def minDepth(self, root):
        if not root: 
            return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        return l + r + 1 if l == 0 or r == 0 else min(l, r) + 1 


    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right: 
            return 1
        # if no leaf node, should return float("inf"), so that it will return the minimum depth 
        # [1,2] should return 2 instead of 1
        return min(self.minDepth(root.left) if root.left else float("inf"), self.minDepth(root.right) if root.right else float("inf")) + 1

if __name__ == '__main__':
    T = TreeNode
    root = T(1, T(2), T(3,T(4)))
    s = Solution()
    print(s.minDepth(root))    
