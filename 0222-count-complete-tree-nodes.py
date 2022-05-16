# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return 1+self.countNodes(root.left)+self.countNodes(root.right)

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = [root]
        cnt = 0
        while level:
            cnt += len(level)
            level = [c for node in level for c in (node.left, node.right) if c]
        return cnt

    def countNodes(self, root: TreeNode) -> int:
        def depth(node):
            return 0 if node == None else 1+depth(node.left)
        if not root: return 0
        ld = depth(root.left)
        rd = depth(root.right)
        print(ld, rd)
        if ld == rd: # left tree is full
            #2**ld => node number of left subtree plus root
            #countnodes(root.right) count the number of right subtree
            return 2**ld + self.countNodes(root.right)
        else: # right tree is full
            return 2**rd + self.countNodes(root.left)

if __name__ == '__main__':
    s = Solution()
    print(s.countNodes([1,2,3,4,5,6]) == 6)
