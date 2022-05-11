"""
preorder: node + left + right

Time complexity : we visit each node exactly once, thus the time complexity is O(N), where N is the number of nodes, i.e. the size of tree.

Space complexity : depending on the tree structure, we could keep up to the entire tree, therefore, the space complexity is O(N).

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # BFS
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return 
        stack, ans = [root], []
        while stack:
            node = stack.pop()
            ans.append(node.val)  # node + left + right
            if node.right: stack.append(node.right)
            if node.left:  stack.append(node.left)
        return ans

    # 统一写法 BFS
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        stack, res = [root], []
        while stack:
            top = stack[-1]
            if top != None:
                node = stack.pop()
                if node.right: stack.append(node.right)
                if node.left: stack.append(node.left)
                stack.append(node)
                stack.append(None)
            else:
                stack.pop() # pop the None
                node = stack.pop()
                res.append(node.val)
        return res

    # DFS - recursion
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def helper(cur):
            if cur == None:
                return
            res.append(cur.val)
            helper(cur.left)
            helper(cur.right)
        helper(root)
        return res

    # DFS - recursion
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []

if __name__ == '__main__':
    s = Solution()
    print(s.preorderTraversal([1,null,2,3]) == [1,2,3])



