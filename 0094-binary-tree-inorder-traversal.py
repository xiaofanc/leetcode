"""
我们以中序遍历为例，在二叉树中提到说使用栈的话，无法同时解决访问节点（遍历节点）和处理节点（将元素放进结果集）不一致的情况。
那我们就将访问的节点放入栈中，把要处理的节点也放入栈中但是要做标记。
如何标记呢，就是要处理的节点放入栈之后，紧接着放入一个空指针作为标记。 这种方法也可以叫做标记法。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 统一写法 BFS
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        stack, res = [root], []
        while stack:
            top = stack[-1]
            if top != None:
                node = stack.pop()
                if node.right: stack.append(node.right)
                stack.append(node)
                stack.append(None) # 标记要处理的节点
                if node.left: stack.append(node.left)
            else:
                stack.pop() # pop the None
                node = stack.pop()
                res.append(node.val)
        return res

    # DFS
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans, stack = [], []
        def pushleft(node):
            # in order to pop left node first
            while node:
                stack.append(node)
                node = node.left
        pushleft(root) #root, root.left, root.left.left...
        while stack:
            top = stack.pop()   # node.left
            ans.append(top.val) # node.left
            # if node has right subtree, output the right substree
            # if node does not have right subtree, then it will output the parent node
            pushleft(top.right) # node.left.right
        return ans

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root
        stack = []
        cur = root
        res = []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res
            
    # DFS - recursion
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []        
    
    # DFS - recursion
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def helper(cur):
            if not cur:
                return
            helper(cur.left)
            res.append(cur.val)
            helper(cur.right)
        helper(root)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.inorderTraversal([1,null,2,3]) == [1, 3, 2])


    