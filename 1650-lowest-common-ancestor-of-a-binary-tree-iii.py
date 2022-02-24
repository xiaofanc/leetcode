
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        n1, n2 = p, q
        while n1 != n2:
            n1 = n1.parent if n1 else q
            n2 = n2.parent if n2 else p
        return n1

if __name__ == '__main__':
    s = Solution()
    print(s.lowestCommonAncestor([3,5,1,6,2,0,8,null,null,7,4],5,1))  # 3
    print(s.lowestCommonAncestor([3,5,1,6,2,0,8,null,null,7,4],5,4))  # 4
