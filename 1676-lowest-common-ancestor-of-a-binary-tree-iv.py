# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodeset = set(nodes)
        
        def DFS(root):
            if not root:
                return root
            if root in nodeset:
                return root
            l = DFS(root.left)
            r = DFS(root.right)
            if l and r:
                return root
            return l or r
        return DFS(root)


if __name__ == '__main__':
    s = Solution()
    print(s.lowestCommonAncestor([3,5,1,6,2,0,8,null,null,7,4],[5,1])) # 3
       