"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

level-order tranversal, add the last val

Time complexity is the same O(N) both for DFS and BFS since one has to visit all nodes.
Space: O(N)

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        frontier = [root]
        ans = []
        # BFS
        while frontier:
            ans.append(frontier[-1].val)
            frontier = [n for f in frontier for n in (f.left, f.right) if n]
        return ans

    # BFS
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        level = deque([root])
        while level:
            l = len(level)
            for _ in range(l):
                node = level.popleft()
                if node.left: level.append(node.left)
                if node.right: level.append(node.right)
            res.append(node.val)
        return res

    # DFS - recursion
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def helper(node, depth):
            if not node:
                return []
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)
            if node.left:
                helper(node.left, depth+1)
            if node.right:
                helper(node.right, depth+1)
        helper(root, 0)
        res = [r[-1] for r in res]
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.rightSideView([1,2,3,null,5,null,4]) == [1, 3, 4])
    print(s.rightSideView([1,2,3,null,5,2,4,-1]) == [1, 3, 4, -1])