"""
遇到这个题目首先想的是要是能自底向上查找就好了，这样就可以找到公共祖先了。
那么二叉树如何可以自底向上查找呢？
回溯啊，二叉树回溯的过程就是从低到上。
后序遍历就是天然的回溯过程，最先处理的一定是叶子节点。

首先最容易想到的一个情况：如果找到一个节点，发现左子树出现结点p，右子树出现节点q，或者 左子树出现结点q，右子树出现节点p，那么该节点就是节点p和q的最近公共祖先。
但是很多人容易忽略一个情况，就是节点本身p(q)，它拥有一个子孙节点q(p)。
使用后序遍历，回溯的过程，就是从低向上遍历节点，一旦发现满足第一种情况的节点，就是最近公共节点了。
但是如果p或者q本身就是最近公共祖先呢？
其实只需要找到一个节点是p或者q的时候，直接返回当前节点，无需继续递归子树。如果接下来的遍历中找到了后继节点满足第一种情况则修改返回值为后继节点，否则，继续返回已找到的节点即可。

在递归函数有返回值的情况下：如果要搜索一条边，递归函数返回值不为空的时候，立刻返回，如果搜索整个树，直接用一个变量left、right接住返回值，这个left、right后序还有逻辑处理的需要，也就是后序遍历中处理中间节点的逻辑（也是回溯）。

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right))
        return root if left and right else left or right

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q): return root
        left  = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if (left and right) else (left or right)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return node
            if node == p or node == q:
                return node
            l = dfs(node.left)
            r = dfs(node.right)
            if l and r: return node
            return l or r
        return dfs(root)


if __name__ == '__main__':
    s = Solution()
    print(s.lowestCommonAncestor([3,5,1,6,2,0,8,null,null,7,4],5,1)) # 3
    


