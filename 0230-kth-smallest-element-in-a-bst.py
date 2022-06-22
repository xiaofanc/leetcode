# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(node):
            if not node: return []  # important
            return inorder(node.left) + [node.val] + inorder(node.right)
        nums = inorder(root)
        return nums[k-1] # the first smallest number has index 0

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def gen(node):
            if not node: return None
            yield from gen(node.left)
            yield node.val
            yield from gen(node.right)
        ans = None
        g = gen(root)
        for i in range(k):
            ans = next(g)
        return ans

    # recursion
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # use inorder traversal to traverse the tree
        def inorder(node):
            nonlocal k
            if not node: # if node condition fails if node is 0
                return 0
            left = inorder(node.left)
            k -= 1
            if not k:
                return node.val
            right = inorder(node.right)
            return left or right
        return inorder(root)

    # return None !!!
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # use inorder traversal to traverse the tree
        def inorder(node):
            nonlocal k
            if not node: # if node condition fails if node is 0
                return 0
            inorder(node.left)
            k -= 1
            if not k:
                return node.val
            inorder(node.right)
        return inorder(root)

if __name__ == '__main__':
    s = Solution()
    print(s.kthSmallest([3,1,4,null,2], 1) == 1)
    print(s.kthSmallest([3,0,4,null,2], 1) == 0)


    


