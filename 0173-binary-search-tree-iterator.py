# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        # 先把所有的左children加进去
        self.stack = []
        node = root
        while node:
            self.stack.append(node)
            node = node.left
            
    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.stack:
            # 总是把左边的children先pop出来
            cur = self.stack.pop()
            # 如果pop出来的左children有右子树
            node = cur.right
            while node:
                # 把右子树加进去
                self.stack.append(node)
                #把右子树的左children都进去
                node = node.left
            return cur.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.stack != []


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()