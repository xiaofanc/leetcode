"""
题目中要求在二叉搜索树上任意两节点的差的绝对值的最小值。

注意是二叉搜索树，二叉搜索树可是有序的。

遇到在二叉搜索树上求什么最值啊，差值之类的，就把它想成在一个有序数组上求最值，求差值，这样就简单多了。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nodes = []
        def traversal(node):
            if not node:
                return
            traversal(node.left)
            nodes.append(node.val)
            traversal(node.right)
        traversal(root)
        mindiff = float("inf")
        for i in range(1, len(nodes)):
            mindiff = min(mindiff, nodes[i]-nodes[i-1])
        return mindiff

    # inorder traversal - recursion
    # 既然是搜索树，它中序遍历就是有序的
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nodes = []
        mindiff = float("inf")
        prev = TreeNode(None)
        def traversal(node):
            nonlocal prev, mindiff
            if not node:
                return
            traversal(node.left)
            if prev.val != None and node.val - prev.val < mindiff:
                mindiff = node.val - prev.val
            prev = node
            traversal(node.right)
        traversal(root)
        return mindiff

    # inorder traversal - iterative
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        mindiff = float("inf")
        prev, cur = None, root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()  # the smallest element
                if prev:
                    mindiff = min(mindiff, cur.val-prev.val)
                prev = cur
                cur = cur.right
        return mindiff


    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        stack = [root]
        prev = None
        minDiff = float("inf")
        while stack:
            top = stack[-1]
            if top:
                node = stack.pop()
                if node.right: stack.append(node.right)
                stack.append(node)
                stack.append(None)
                if node.left: stack.append(node.left)
            else:
                stack.pop()
                r = stack.pop()
                if prev != None:  # if prev does not work when prev == 0
                    minDiff = min(minDiff, abs(r.val-prev))
                prev = r.val
        return minDiff

if __name__ == '__main__':
    s = Solution()
    print(s.getMinimumDifference([0,null,2236,1277,2776,519])) # 0 as prev





