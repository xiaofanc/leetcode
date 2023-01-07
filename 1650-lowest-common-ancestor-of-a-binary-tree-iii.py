
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

This solution is mind blowing. The idea is this say p to root is path length is a + c and q to root path length is b + c where c is the length of the common path to root after they meet. Then we are just making them both travel the same distance a + b +c by this swapping when root trick. So they exactly meet at that common merging point which is the LCA.
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        n1, n2 = p, q
        while n1 != n2:
            n1 = n1.parent if n1 else q
            n2 = n2.parent if n2 else p
        return n1

    # The idea is to store the parents (path) from root to p, and then check q's path.
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visited = set()
        while p:
            visited.add(p.val)
            p = p.parent
        
        while q:
            if q.val in visited:
                return q
            q = q.parent
        return None

    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def getDepth(node, depth):
            if not node:
                return depth
            return getDepth(node.parent, depth+1)
        
        pd = getDepth(p, 0)
        qd = getDepth(q, 0)

        # move to the same level
        if pd > qd:
            for i in range(pd-qd):
                p = p.parent
        elif pd < qd:
            for i in range(qd-pd):
                q = q.parent
        
        # move up together
        while p != q:
            p = p.parent
            q = q.parent
        return p
        
if __name__ == '__main__':
    s = Solution()
    print(s.lowestCommonAncestor([3,5,1,6,2,0,8,null,null,7,4],5,1))  # 3
    print(s.lowestCommonAncestor([3,5,1,6,2,0,8,null,null,7,4],5,4))  # 4
