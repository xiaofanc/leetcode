# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    # BFS - explore all nodes in the same level
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        frontier = [root]
        ans = []
        while frontier:
            ans.append(f.val for f in frontier)
            frontier = [n for f in frontier for n in (f.left, f.right) if n]
        return ans

    # BFS
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level = deque([root])
        results = []
        while level:
            res = []
            for _ in range(len(level)):
                node = level.popleft()
                res.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            results.append(res)
        return results

    # recursion - DFS: stack
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def helper(node, depth):
            if not node:
                return []
            if len(res) == depth: res.append([]) # init
            res[depth].append(node.val)
            if node.left: 
                helper(node.left, depth+1)
            if node.right:
                helper(node.right, depth+1)
        helper(root, 0)
        return res

    # return [3, 9, 20, 15, 7]
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return None
        frontier = [root]
        ans = []
        while frontier:
            for node in frontier:
                ans.append(node.val)
            frontier = [n for f in frontier for n in (f.left, f.right) if n]
        return ans
        
if __name__ == '__main__':
    s = Solution()
    print(s.levelOrder([3,9,20,null,null,15,7]) == [[3],[9,20],[15,7]])