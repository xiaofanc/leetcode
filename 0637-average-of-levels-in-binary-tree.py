# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root == None: return []
        frontier = [root]
        avg = []
        while frontier:
            avg.append(sum(f.val for f in frontier)/len(frontier))
            frontier = [n for f in frontier for n in (f.left, f.right) if n]
        return avg

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

if __name__ == '__main__':
    s = Solution()
    print(s.averageOfLevels())