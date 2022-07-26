from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLeaves(self, root):
        res = []
        def getHeight(node):
            if not node:
                return -1
            return 1 + max(getHeight(node.left), getHeight(node.right))
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append((getHeight(node), node.val))
            dfs(node.right)
        
        dfs(root)
        maxh = getHeight(root)
        ans = []
        for i in range(maxh+1):
            ans.append([])
        for h, val in res:
            ans[h].append(val)
        return ans

    def findLeaves(self, root):
        res = []
        def getHeight(node):
            if not node:
                return -1
            lefth = getHeight(node.left)
            righth = getHeight(node.right)
            currh = 1 + max(lefth, righth)
            if len(res) == currh:
                res.append([])
            res[currh].append(node.val)
            return currh
        
        getHeight(root)
        return res


    def findLeaves(self, root):
        distances = defaultdict(list)
        
        def postorder(r):
            if not r:
                return 0
            left = postorder(r.left)
            right = postorder(r.right)
            distance = max(left, right)
            distances[distance].append(r.val)
            return 1 + distance
        
        postorder(root)
        # print(distances) # {0: [4, 5, 3], 1: [2], 2: [1]}
        return distances.values()

    def findLeaves(self, root):
        output = defaultdict(list)

        def dfs(node, layer):
            if not node: 
                return layer # same as return -1
            print("node, layer", node.val, layer)
            # node, layer 1 0
            # node, layer 2 0
            # node, layer 4 0
            # node, layer 5 0
            # node, layer 3 0
            left = dfs(node.left, layer)
            right = dfs(node.right, layer)
            layer = max(left, right)
            output[layer].append(node.val)
            return layer + 1

        dfs(root, 0)
        return output.values() 

if __name__ == '__main__':
    T = TreeNode
    root = T(1, T(2), T(3,T(4)))
    root = T(1, T(2, T(4), T(5)), T(3))
    s = Solution()
    print(s.findLeaves(root)) # [[2, 4], [3], [1]]
            