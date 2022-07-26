"""
Three rules:
- root's right node becomes the left node of the left node of root
- root becomes the right node of root's left node
- above rules apply on the left edge and return left node along the path.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
    	return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')

class Solution:
	# recursive bottom-up
    def upsideDownBinaryTree(self, root):
        
        # Termination Condition
        if not root or (not root.left and not root.right):
            return root
        
        # The original left child becomes the new root.
        left = self.upsideDownBinaryTree(root.left)
        
        # The original right child becomes the new left child.
        root.left.left = root.right
        
        # The original root becomes the new right child.
        root.left.right = root
        
        root.left = None
        root.right = None
        
        # The original left child becomes the new root.
        return left

    # recursive top-down
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.root = None
        def dfs(node, par, right):
            if not node:
                return
            
            _left = node.left
            _right = node.right
            node.left = right
            node.right = par

            if _left:
                dfs(_left, node, _right)
            else:
                self.root = node

        dfs(root, None, None)
        return self.root

    # iterative top-down
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        new_root = None
        par = None
        right = None
        
        while root:
            # update current level
            _left = root.left
            _right = root.right
            root.left = right
            root.right = par
            
            # move to the next level
            if _left:
                par = root
                root = _left
                right = _right
            # reach the left leaf
            else:
                new_root = root
                break
        return new_root

if __name__ == '__main__':
    T = TreeNode
    root = T(1, T(2, T(4), T(5)), T(3))
    s = Solution()
    print(s.upsideDownBinaryTree(root)) # N(4, N(5, , ), N(2, N(3, , ), N(1, , )))

