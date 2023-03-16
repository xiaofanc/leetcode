class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')

class Solution:
    def isSymmetric0(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            return self.helper(root.left, root.right)
        
    def helper(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:
            outpair = self.helper(left.left, right.right)
            inpair = self.helper(left.right, right.left)
            return outpair and inpair
        else:
            return False

    def isSymmetric1(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [[root.left, root.right]]
        while len(stack) > 0:
            pair = stack.pop(0)
            left = pair[0]
            right = pair[1]
            
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.insert(0,[left.left, right.right])
                stack.insert(0,[left.right, right.left])
            else:
                return False
        return True


    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def helper(l, r):
            if not l and not r:
                return True
            elif not l and r:
                return False
            elif not r and l:
                return False
            else:
                return l.val == r.val and helper(l.left, r.right) and helper(l.right, r.left)
            
        return helper(root.left, root.right)
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        q.append(root)
        while q:
            n1, n2 = q.popleft(), q.popleft()
            if not n1 and not n2:
                continue
            if not n1 or not n2:
                return False
            if n1.val != n2.val:
                return False
            q.append(n1.left)
            q.append(n2.right)
            q.append(n1.right)
            q.append(n2.left)
        return True
        
if __name__ == '__main__':
    T = TreeNode
    t1 = T(1, T(2,T(3),T(4)), T(2,T(4),T(3)))
    print(t1)
   
    s=Solution()
    print(s.isSymmetric0(t1))
    print(s.isSymmetric1(t1))
