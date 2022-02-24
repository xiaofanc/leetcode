class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_node = root.val
        p_val = p.val
        q_val = q.val
        if p_val < parent_node and q_val < parent_node:
            # they are both in left subtree
            return self.lowestCommonAncestor(root.left, p, q)
        elif p_val > parent_node and q_val > parent_node:
            return self.lowestCommonAncestor(root.right, p, q)
        else:   # when p, q are in both sides, then root is the lowest common ancestor
            return root.val
    
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        p_val = p.val
        q_val = q.val
        while node:
            parent_node = node.val
            if p_val < parent_node and q_val < parent_node:
                # they are both in left subtree
                node = node.left
            elif p_val > parent_node and q_val > parent_node:
                node = node.right
            else:   # when p, q are in both sides, then root is the lowest common ancestor
                return node.val              
            
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val: p, q = q, p
        node = root
        while node:
            if node.val < p.val:
                node = node.right
            elif p.val <= node.val <= q.val:
                return node
            else:
                node = node.left

if __name__ == '__main__':
    T = TreeNode
    root = T(6, T(2, T(0), T(4, T(3), T(5))), T(8,T(7),T(9)))
    print(root)
    s = Solution()
    print(s.lowestCommonAncestor(root, T(2),T(8))) #6
    print(s.lowestCommonAncestor(root, T(2),T(4))) #2
    print(s.lowestCommonAncestor(root, T(0),T(5))) #2