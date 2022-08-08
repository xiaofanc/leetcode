"""
在有序树里，如果判断一个节点的左子树里有p，右子树里有q呢？
其实只要从上到下遍历的时候，cur节点是数值在[p, q]区间中则说明该节点cur就是最近公共祖先了。
和236不同，普通二叉树求最近公共祖先需要使用回溯，从底向上来查找，二叉搜索树就不用了，因为搜索树有序（相当于自带方向），那么只要从上向下遍历就可以了。

确定单层递归的逻辑：
在遍历二叉搜索树的时候就是寻找区间[p->val, q->val]（注意这里是左闭又闭）
- 如果 cur->val 大于 p->val，同时 cur->val 大于q->val，那么就应该向左遍历（说明目标区间在左子树上）。
- 如果 cur->val 小于 p->val，同时 cur->val 小于 q->val，那么就应该向右遍历（目标区间在右子树）。
- 剩下的情况，那么cur就是最近公共祖先了，直接返回cur。

"""
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')


class Solution:
    # 普通二叉树求公共祖先: O(N)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right

    # optimized dfs: O(logN)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_node = root.val
        p_val = p.val
        q_val = q.val
        if p_val < parent_node and q_val < parent_node:
            # they are both in left subtree
            return self.lowestCommonAncestor(root.left, p, q)
        elif p_val > parent_node and q_val > parent_node:
            return self.lowestCommonAncestor(root.right, p, q)
        # when p, q are in both sides, then root is the lowest common ancestor
        else:   
            return root.val
    
    # iterative
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else: # p and q are in both sides or p/q is the root
                return cur             
            
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




    