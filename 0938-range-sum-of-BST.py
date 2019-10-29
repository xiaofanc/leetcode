class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')

class Solution:
    def rangeSumBST0(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        if R < root.val:
            return self.rangeSumBST0(root.left, L, R)
        elif L > root.val:
            return self.rangeSumBST0(root.right, L, R)
        else:
            return self.rangeSumBST0(root.left, L, R) + root.val + self.rangeSumBST0(root.right, L, R)


    def rangeSumBST1(self, root: TreeNode, L: int, R: int) -> int:
        def traverse(node):
            if node == None:
                return 
            yield from traverse(node.left)
            yield node.val
            yield from traverse(node.right)
        s = sum(i for i in traverse(root) if L <= i <= R)
        return s

    def rangeSumBST2(self, root: TreeNode, L: int, R: int) -> int:
    	l = (self.rangeSumBST2(root.left, L, R) if root.left != None else 0)
    	r = (self.rangeSumBST2(root.right, L, R) if root.right != None else 0)
    	m = root.val
    	return  l + (m if (L <= m and m <= R) else 0) + r

if __name__ == '__main__':
    T = TreeNode
    t1 = T(10, T(5,T(3),T(7)), T(15,None,T(18)))
    print(t1)

    s=Solution()
    print(s.rangeSumBST0(t1,7, 15))
    print(s.rangeSumBST1(t1,7, 15))
    print(s.rangeSumBST2(t1,7, 15))

