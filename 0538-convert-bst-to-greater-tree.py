"""
给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。
那么有序的元素如果求累加呢？

其实这就是一棵树，大家可能看起来有点别扭，换一个角度来看，这就是一个有序数组[2, 5, 13]，求从后到前的累加数组，也就是[20, 18, 13]，是不是感觉这就简单了。
从树中可以看出累加的顺序是右中左，所以我们需要反中序遍历这个二叉树，然后顺序累加就可以了。
"""
class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.total = 0
        def trans(node):
            if not node: return 0
            trans(node.right)
            self.total += node.val
            node.val = self.total
            trans(node.left)
        trans(root)
        return root

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pre = None
        def traversal(node):
            nonlocal pre
            if not node:
                return node
            traversal(node.right)
            if pre:
                node.val += pre.val
            pre = node
            traversal(node.left)
        traversal(root)
        return root

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # iterative 反中序遍历
        prev, cur = None, root
        stack = []
        while cur or stack:
            if cur:  # push right node to the stack
                stack.append(cur)
                cur = cur.right
            else:
                node = stack.pop()
                if prev:
                    node.val += prev
                prev = node.val
                cur = node.left # push the left subtree of the node
        return root
        
if __name__ == '__main__':
    s = Solution()
    print(s.convertBST([5,2,13]) == [18,20,13]) 
    print(s.convertBST([4,2,5,1,3]) == [9,14,5,15,12]) 
                
                
                
