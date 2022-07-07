# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: # Time: O(n) One complete traversal for leaves and two traversals up to depth of binary tree for left and right boundary
    def isleaf(self, root):
        if not root.right and not root.left:
            return True
        return False
    
    def addleaves(self, res, root): # For this problem, the root is not a leaf
        if root and self.isleaf(root):
            res.append(root.val)
        else:
            if root.left:
                self.addleaves(res, root.left)
            if root.right:
                self.addleaves(res, root.right)
        return res
    
    def boundaryOfBinaryTree(self, root):
        # left boundary + leaves + reversed right boundary
        res = []
        if not root:
            return res

        # add left boundary
        if (not self.isleaf(root)):
            res.append(root.val)
        left = root.left
        while left:
            if (not self.isleaf(left)):
                res.append(left.val)
            if left.left:
                left = left.left
            else:
                left = left.right
        
        # add leaves
        self.addleaves(res, root)
        
        # add right boundary
        stack = []
        right = root.right
        while right:
            if (not self.isleaf(right)):
                stack.append(right.val)
            if right.right:
                right = right.right
            else:
                right = right.left
        
        while stack:
            res.append(stack.pop())
            
        return res
            
if __name__ == '__main__':
    T = TreeNode
    root = T(1, None, T(2, T(3), T(4))) 
    s = Solution()
    print(s.boundaryOfBinaryTree(root)) # [1,3,4,2]



