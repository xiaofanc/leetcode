# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        visited = dict()
        cache = {}
        
        def serialize(root): 
            # use cache to only serialize node once
            if root in cache:
                return cache[root]
            cache[root] = '^' + str(root.val) + serialize(root.left) + serialize(root.right) if root else 'N'
            return cache[root] 
        
        def helper(node):
            if not node:
                return None
            # serialize each node to see if pattern exists
            subtree = serialize(node)
            visited[subtree] = visited.get(subtree, 0) + 1
            # if repeated more than 2 times, do not add
            if visited[subtree] == 2: 
                res.append(node)
            helper(node.left)
            helper(node.right)
        helper(root)
        
        return res

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        visited = defaultdict(list)
        res = []
        
        def serialize(root): # O(N)
            if not root:
                return 'N'
            # '^' to seprate 1 11 / 11 1
            s = '^' + str(root.val) + serialize(root.left) + serialize(root.right)
            visited[s].append(root)
            return s
        
        serialize(root)
        for k, v in visited.items():
            if len(v) > 1:
                res.append(v[0])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.findDuplicateSubtrees([2,1,11,11,null,1])) # []


    
