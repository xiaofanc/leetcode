"""

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

不能单纯的比较左节点小于中间节点，右节点大于中间节点就完事了。
我们要比较的是 左子树所有节点小于中间节点，右子树所有节点大于中间节点。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time: O(N)
    def isValidBST(self, root: TreeNode) -> bool:  # time O(n)
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            v = node.val
            if v <= lower or v >= upper:
                return False
            
            if not helper(node.left, lower, v):  # leftsubtree < root.val
                return False
            if not helper(node.right, v, upper): # rightsubtree > root.val
                return False
            return True
        return helper(root)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lower, upper = -float("inf"), float("inf")
        def helper(node, lower, upper):
            if not node:
                return True
            if node.val > lower and node.val < upper:
                return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)
            return False
        return helper(root, lower, upper)

    # inorder traversal
    # 既然是搜索树，它中序遍历就是有序的
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        maxval = -float("inf")
        
        def helper(node):
            nonlocal maxval
            if not node:
                return True
            left = helper(node.left)
            # 中序遍历，验证遍历的元素是不是从小到大
            if maxval >= node.val:
                return False
            else:
                maxval = node.val
            right = helper(node.right)
            return left and right
        
        return helper(root)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = TreeNode(None)
        def traversal(node):
            nonlocal prev
            if not node:
                return True
            left = traversal(node.left)
            if prev.val != None and node.val <= prev.val:
                return False
            else:
                prev = node
            right = traversal(node.right)
            return left and right
        return traversal(root)

    # stack
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: 
            return True
        
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue  # !!! not return True
            v = root.val
            if v <= lower or v >= upper:
                return False
            stack.append((root.left, lower, v))
            stack.append((root.right, v, upper))
        return True

    # inorder traversal
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        cur = root
        prev = None
        while cur or stack:
            if cur: # 指针来访问节点，访问到最底层
                stack.append(cur)
                cur = cur.left
            else: # 逐一处理节点
                cur = stack.pop()
                # 比较当前节点和前节点的值的大小
                if prev and prev.val >= cur.val:
                    return False
                prev = cur
                cur = cur.right
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isValidBST([10,5,15,null,null,6,20]))  #false



    