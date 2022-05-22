"""
Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

既然是搜索树，它中序遍历就是有序的。
遍历有序数组的元素出现频率，从头遍历，那么一定是相邻两个元素作比较，然后就把出现频率最高的元素输出就可以了。
弄一个指针指向前一个节点，这样每次cur（当前节点）才能和pre（前一个节点）作比较。
而且初始化的时候pre = NULL，这样当pre为NULL时候，我们就知道这是比较的第一个元素。
此时又有问题了，因为要求最大频率的元素集合（注意是集合，不是一个元素，可以有多个众数），如果是数组上大家一般怎么办？
应该是先遍历一遍数组，找出最大频率（maxCount），然后再重新遍历一遍数组把出现频率为maxCount的元素放进集合。（因为众数有多个）
这种方式遍历了两遍数组。

那么我们遍历两遍二叉搜索树，把众数集合算出来也是可以的。
但这里其实只需要遍历一次就可以找到所有的众数。
那么如何只遍历一遍呢？
如果 频率count 等于 maxCount（最大频率），当然要把这个元素加入到结果集中（以下代码为result数组）
是不是感觉这里有问题，result怎么能轻易就把元素放进去了呢，万一，这个maxCount此时还不是真正最大频率呢。
所以下面要做如下操作：
频率count 大于 maxCount的时候，不仅要更新maxCount，而且要清空结果集（以下代码为result数组），因为结果集之前的元素都失效了。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
	# 普通二叉树求众数
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        nodes = defaultdict()
        def traversal(node):
            if not node:
                return
            traversal(node.left)
            nodes[node.val] = nodes.get(node.val, 0) + 1
            traversal(node.right)
        traversal(root)
        maxfreq = max(nodes.values())
        res = []
        for key, value in nodes.items():
            if value == maxfreq:
                res.append(key)
        return res

    # BST, no dictionary, recursion
    # 不消耗多余空间
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        maxcount = 0
        count = 0
        res = []
        prev = TreeNode(None)
        def traversal(node):
            nonlocal maxcount, prev, res, count
            if not node:
                return
            traversal(node.left)
            if prev.val == None:
                count = 1
            elif node.val == prev.val:
                count += 1
            elif node.val != prev.val:
                count = 1
            prev = node
            if count > maxcount:
                res = []
                res.append(node.val)
                maxcount = count
            elif count == maxcount:
                res.append(node.val)
            traversal(node.right)
        traversal(root)
        return res

    # BST, iterative
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        maxcount = 0
        count = 0
        res = []
        prev = None
        cur = root
        stack = []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if not prev:
                    count = 1
                elif prev.val == cur.val:
                    count += 1
                else:
                    count = 1
                # compare the frequency
                if count > maxcount:
                    res = [cur.val]
                    maxcount = count
                elif count == maxcount:
                    res.append(cur.val)
                prev = cur
                cur = cur.right # inorder traversal
        return res

