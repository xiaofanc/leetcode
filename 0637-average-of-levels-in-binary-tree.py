# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# time: O(N), space: O(N)
class Solution:
    # BFS
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root == None: return []
        frontier = [root]
        avg = []
        while frontier:
            avg.append(sum(f.val for f in frontier)/len(frontier))
            frontier = [n for f in frontier for n in (f.left, f.right) if n]
        return avg

    # BFS
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        res = []
        level = deque([root])
        while level:
            r = 0
            size = len(level)
            for _ in range(size):
                node = level.popleft()
                r += node.val
                if node.left: level.append(node.left)
                if node.right: level.append(node.right)
            res.append(r/size)
        return res

    #DFS 先走左子树， 走完返回root 再走右子树
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        self.levels = defaultdict(list)
        def traverse(node, level):
            if node == None:
                return
            self.levels[level].append(node.val)
            if node.left:
                traverse(node.left, level+1)
            if node.right:
                traverse(node.right, level+1)
        traverse(root, 0)
        return [sum(self.levels[i])/len(self.levels[i]) for i in range(len(self.levels))]

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        res = []
        def helper(node, depth):
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)
            if node.left:
                helper(node.left, depth+1)
            if node.right:
                helper(node.right, depth+1)
        helper(root, 0)
        for i, n in enumerate(res):
            res[i] = sum(res[i]) / len(res[i])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.averageOfLevels([3,9,20,null,null,15,7])) # [3.00000,14.50000,11.00000]



