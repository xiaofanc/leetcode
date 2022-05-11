# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans, stack = [], []
        def pushleft(node):
            # in order to pop left node first
            while node:
                stack.append(node)
                node = node.left
        pushleft(root) #root, root.left, root.left.left...
        while stack:
            top = stack.pop()   # node.left
            ans.append(top.val) # node.left
            # if node has right subtree, output the right substree first
            # if node does not have right subtree, then it will output the parent node
            pushleft(top.right) # node.left.right
        return ans
            
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []        
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def helper(cur):
            if not cur:
                return
            helper(cur.left)
            res.append(cur.val)
            helper(cur.right)
        helper(root)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.inorderTraversal([1,null,2,3]) == [1, 3, 2])


    