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

if __name__ == '__main__':
    T = TreeNode
    t1 = T(1, T(2,T(3),T(4)), T(2,T(4),T(3)))
    print(t1)
   
    s=Solution()
    print(s.isSymmetric0(t1))
    print(s.isSymmetric1(t1))
