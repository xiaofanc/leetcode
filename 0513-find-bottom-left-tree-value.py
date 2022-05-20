# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        level = deque([root])
        while level:
            size = len(level)
            res = []
            for i in range(size):
                node = level.popleft()
                res.append(node.val)
                for c in [node.left, node.right]:
                    if c:
                        level.append(c)
                # level = [c for node in level for c in [node.left, node.right] if c]
        return res[0]

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        level = [root]
        while level:
            res = [node.val for node in level]
            level = [c for node in level for c in [node.left, node.right] if c]
        return res[0]

    # recursion
    # 当遇到叶子节点的时候，就需要统计一下最大的深度了，所以需要遇到叶子节点来更新最大深度
    # 那么如果找最左边的呢？可以使用前序遍历，这样才先优先左边搜索，然后记录深度最大的叶子节点，此时就是树的最后一行最左边的值
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        maxdepth, leftmostvalue = -float("inf"), 0
        def traversal(node, depth):
            # 全局变量
            nonlocal maxdepth, leftmostvalue
            if not node.left and not node.right:
                if depth > maxdepth:
                    maxdepth = depth
                    leftmostvalue = node.val
            if node.left:
                depth += 1
                traversal(node.left, depth)  # traversal(node.left, depth+1)
                depth -= 1
            if node.right:
                depth += 1
                traversal(node.right, depth)
                depth -= 1
        traversal(root, 0)
        return leftmostvalue




