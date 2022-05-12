"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    # BFS
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        level = [root]
        res = []
        while level:
            res.append([node.val for node in level])
            level = [c for node in level for c in node.children if c]
        return res

    # BFS
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        level = deque([root])
        results = []
        while level:
            size = len(level)
            res = []
            for _ in range(size):
                node = level.popleft()
                res.append(node.val)
                if node.children:
                    level.extend(node.children)
            results.append(res)
        return results

    # DFS
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        def helper(node, depth):
            if len(res) == depth:
                res.append([])
            for n in node:
                res[depth].append(n.val)
                if n.children:
                    helper(n.children, depth+1)
        helper([root], 0)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.levelOrder([1,null,3,2,4,null,5,6])) # [[1],[3,2,4],[5,6]]




    

