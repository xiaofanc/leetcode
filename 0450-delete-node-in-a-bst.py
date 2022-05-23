"""
确定终止条件:
遇到空返回，其实这也说明没找到删除的节点，遍历到空节点直接返回了
确定单层递归的逻辑:
第一种情况：没找到删除的节点，遍历到空节点直接返回了
找到删除的节点:
第二种情况：左右孩子都为空（叶子节点），直接删除节点， 返回NULL为根节点
第三种情况：删除节点的左孩子为空，右孩子不为空，删除节点，右孩子补位，返回右孩子为根节点
第四种情况：删除节点的右孩子为空，左孩子不为空，删除节点，左孩子补位，返回左孩子为根节点
第五种情况：左右孩子节点都不为空，则将删除节点的左子树头结点（左孩子）放到删除节点的右子树的最左面节点的左孩子上，返回删除节点右孩子为新的根节点。
what if remove root?

普通二叉树的删除方式（没有使用搜索树的特性，遍历整棵树），用交换值的操作来删除目标节点。
代码中目标节点（要删除的节点）被操作了两次：
第一次是和目标节点的右子树最左面节点交换。
第二次直接被NULL覆盖了。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val == key:
            if not root.left and not root.right:
                return None
            elif root.left and not root.right:
                return root.left
            elif root.right and not root.left:
                return root.right
            else: 
                cur = root.right
                # 找右子树最左面的节点
                # 将删除节点的左子树头结点（左孩子）放到删除节点的右子树的最左面节点的左孩子上
                while cur.left:
                    cur = cur.left
                cur.left = root.left
                return root.right
        # 这里相当于把新的节点返回给上一层，上一层就要用 root->left 或者 root->right接住
        if root.val > key: root.left = self.deleteNode(root.left, key)
        if root.val < key: root.right = self.deleteNode(root.right, key)
        return root


    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val == key:
            if not root.left and not root.right:
                return None
            elif root.left and not root.right:
                return root.left
            elif root.right and not root.left:
                return root.right
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                # 将删除节点与右子树最左孩子交换值，并删除右子树最左孩子
                root.val = cur.val
                root.right = self.deleteNode(root.right, root.val)
                return root
        if root.val > key: root.left = self.deleteNode(root.left, key)
        if root.val < key: root.right = self.deleteNode(root.right, key)
        return root

    # 普通二叉树的删除方式
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val == key:
            if not root.left and not root.right:
                return None
            elif not root.right:
                return root.left
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                # 将删除节点与右子树最左孩子交换值，并删除右子树最左孩子
                root.val = cur.val
                root.right = self.deleteNode(root.right, root.val)
                return root
        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        return root



