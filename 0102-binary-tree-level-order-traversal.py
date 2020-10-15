# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        frontier = [root]
        ans = []
        while frontier:
            ans.append(f.val for f in frontier)
            frontier = [n for f in frontier for n in (f.left, f.right) if n]
        return ans

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