# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return 
        else:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    #DFS 深度优先搜索
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        else:
            stack = [root]
            while stack:
                node = stack.pop()
                node.left, node.right = node.right, node.left
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return root

    #BFS 广度优先搜索
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = collections.deque([(root)])
        while queue:
            node = queue.popleft() # level order
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root

if __name__ == '__main__':
    s = Solution()
    print(s.invertTree([4,2,7,1,3,6,9]))

