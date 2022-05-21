# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        #find the root based on preorder traversal 
        #then find the index of the root in inorder traversal
        #Left is the left subtree, and right is the right subtree
        if inorder == []:
            return None
        pivot = preorder[0]  # root
        i = inorder.index(pivot)
        node = TreeNode(pivot)
        # split lists based on root, length should be same
        node.left  = self.buildTree(preorder[1:i+1], inorder[0:i])
        node.right = self.buildTree(preorder[i+1:], inorder[i+1:])   
        return node


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def traversal(preorder, inorder):
            if preorder == [] and inorder == []:
                return None         
            # step 1: get the root from preorder list   
            val = preorder[0]
            root = TreeNode(val)
            if len(preorder) == 1:
                return root
            # step 2: find the root in the inorder list
            idx = inorder.index(val)
            # step 4: split preorder and inorder list into two parts based on root
                      # 中序数组大小一定跟前序数组大小是相同的
            # step 5: get the left and right subtree for the root
            root.left = traversal(preorder[1:idx+1], inorder[:idx])
            root.right = traversal(preorder[idx+1:], inorder[idx+1:])
            return root
        
        return traversal(preorder, inorder)






        