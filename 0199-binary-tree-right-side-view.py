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
        #BFS
        while frontier:
            ans.append(frontier[-1].val)
            frontier = [n for f in frontier for n in (f.left, f.right) if n]
        return ans
        
if __name__ == '__main__':
    s = Solution()
    print(s.rightSideView([1,2,3,null,5,null,4]) == [1, 3, 4])
    print(s.rightSideView([1,2,3,null,5,2,4,-1]) == [1, 3, 4, -1])