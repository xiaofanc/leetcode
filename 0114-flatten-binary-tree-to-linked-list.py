# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.flatten(root.left)
        self.flatten(root.right)
        #left subtree is empty
        if root.left == None:
            return 
        else:
            p = root.left
            #find the bottom of left subtree
            while p.right: p = p.right
            #connect right subtree to the bottom of left subtree
            p.right = root.right
            #move left subtree to right
            root.right = root.left
            root.left = None
        return 
            

if __name__ == '__main__':
    s = Solution()
    print(s.flatten([1,2,5,3,4,null,6]) == [1,null,2,null,3,null,4,null,5,null,6])