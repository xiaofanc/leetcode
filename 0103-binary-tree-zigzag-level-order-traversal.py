# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root: return None
        count = 0  # or alternate = False
        frontier = [root]
        while frontier:
            #ans.append([f.val for f in reversed(frontier) if alternate else frontier])
            #alternate = not alternate
            if count%2 == 0:
                ans.append([i.val for i in frontier])  
            else:
                ans.append([i.val for i in reversed(frontier)])
            count += 1
            frontier = [n for f in frontier for n in (f.left, f.right) if n]
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.zigzagLevelOrder([3,9,20,null,null,15,7]) == [[3],[20,9],[15,7]])