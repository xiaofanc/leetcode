"""
第一步：如果数组大小为零的话，说明是空节点了。
第二步：如果不为空，那么取后序数组最后一个元素作为节点元素。
第三步：找到后序数组最后一个元素在中序数组的位置，作为切割点
第四步：切割中序数组，切成中序左数组和中序右数组 （顺序别搞反了，一定是先切中序数组）
第五步：切割后序数组，切成后序左数组和后序右数组
第六步：递归处理左区间和右区间

step 1: if list is empty, return None
        if list has just one element, return that node
step 2: get the last element of postorder list as root
step 3: find index of root in the inorder list and split the inorder list to the left and right part
step 4: use the length of the parts split in the inorder list to split postorder list
step 5: root.left = continue to split the left parts
step 6: root.right = continue to split the right parts
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0 and len(postorder) == 0:
            return None
        def traversal(inorder, postorder):
            if not postorder:
                return None
            val = postorder[-1]
            root = TreeNode(val)
            if len(postorder) == 1:
                return root

            # find the index of the root in the inorder
            idx = inorder.index(val)
            # split inorder list
            left1, right1 = inorder[:idx], inorder[idx+1:]
            # split postorder list
            postorder = postorder[:-1]
            # 中序数组大小一定跟前序数组大小是相同的
            left2, right2 = postorder[:len(left1)], postorder[len(left1):]

            root.left = traversal(left1, left2) 
            root.right = traversal(right1, right2)

            # root.left = traversal(inorder[:idx], postorder[:idx])
            # root.right = traversal(inorder[idx+1:], postorder[idx:-1])
            return root
        return traversal(inorder, postorder)
                
            
