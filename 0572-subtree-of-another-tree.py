class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')

class Solution:
    # DFS
    def isSubtree0(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:  # since we need to keep traversal s until the end
            return False
        if self.ismatch(s, t): return True
        return self.isSubtree0(s.left, t) or self.isSubtree0(s.right, t)
    
    def ismatch(self, s, t):
        if not (s and t):
            return s is t
        return s == t and self.ismatch(s.left, t.left) and self.ismatch(s.right, t.right)

    # convert to string
    # Time: O(|s| + |t|)
    def isSubtree1(self, s: TreeNode, t: TreeNode) -> bool:
        def convert(p):
            return '^' + str(p.val) + '#' + convert(p.left) + convert(p.right) if p else '$'   
        return convert(t) in convert(s)

    # Time: O(|s| * |t|)
    # Space: O(h)
    def isSubtree2(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # for each node of s, let's check if its subtree equals t
        def compare(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2 or node1.val != node2.val:
                return False
            return compare(node1.left, node2.left) and compare(node1.right, node2.right)

        # def compare(node1, node2):
        #     lst = deque()
        #     lst.append(node1)
        #     lst.append(node2)     # lst.extend([node1, node2])
        #     while lst:
        #         n1 = lst.popleft()
        #         n2 = lst.popleft()
        #         if not n1 and not n2:
        #             continue
        #         elif not n1 or not n2 or n1.val != n2.val:
        #             return False 
        #         lst.append(n1.left)    
        #         lst.append(n2.left)
        #         lst.append(n1.right)
        #         lst.append(n2.right)
        #     return True

        if not root:
            return False
        if compare(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

if __name__ == '__main__':
    T = TreeNode
    s = T(1, T(2,T(3),T(4)), T(2,T(4),T(3)))
    t = T(2,T(4),T(3))
    print(t, s)
    s = T(12)  # ^12#$$
    t = T(2)   # ^2#$$   without^, return True is wrong
    s = Solution()

    print(s.isSubtree0(s, t))
    print(s.isSubtree1(s, t))


