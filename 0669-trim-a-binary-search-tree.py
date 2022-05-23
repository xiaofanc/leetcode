"""


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        #root > R
        #root < L
        #root in [L, R]
        def trim(node):
            if not node:
                return None
            elif node.val > R:
                return trim(node.left)
            elif node.val < L:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node
            
        return trim(root)

    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # Base Case
        if not root:
            return None
        # 单层递归逻辑
        # 若当前root节点小于左界：只考虑其右子树，用于替代更新后的其本身，抛弃其左子树整体
        elif root.val < low: 
            return self.trimBST(root.right, low, high)
        # 若当前root节点大于右界：只考虑其左子树，用于替代更新后的其本身，抛弃其右子树整体
        elif root.val > high:
            return self.trimBST(root.left, low, high)
        else:
            # root->left接入符合条件的左孩子
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root       

    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        # 处理头结点，让root移动到[L, R] 范围内，注意是左闭右闭
        while root and (root.val < low or root.val > high):
            if root.val < low:
                root = root.right
            if root.val > high:
                root = root.left
        cur = root
        # 此时root已经在[L, R] 范围内，处理左孩子元素小于L的情况
        while cur:
            while cur.left and cur.left.val < low:
                cur.left = cur.left.right
            cur = cur.left
        cur = root
        # 此时root已经在[L, R] 范围内，处理右孩子大于R的情况
        while cur:
            while cur.right and cur.right.val > high:
                cur.right = cur.right.left
            cur = cur.right
        return root            

if __name__ == '__main__':
    s = Solution()
    print(s.trimBST([1,0,2], 1, 2) == [1,null,2])



