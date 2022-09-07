
class Solution:
	# wrong: "1(1(2(4))(3)"
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = ""
        def preorder(node):
            nonlocal res
            if not node:
                return ""
            if not node.left and not node.right:
                return str(node.val)
            res += str(node.val)
            # 有右孩子或有左孩子，左孩子不能省略
            res += '('
            res += preorder(node.left)
            res += ')'
            # 没有右孩子可以省略
            if node.right:
                res += '('
                res += preorder(node.right)
                res += ')'
            return res
        preorder(root)
        return res
            
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def preorder(node):
            if not node:
                return ""
            if not node.left and not node.right:
                return str(node.val)
            if not node.right:
                return str(node.val) + "(" + preorder(node.left) + ")"
            return str(node.val) + "(" + preorder(node.left) + ")(" + preorder(node.right) + ")"
        return preorder(root)

    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        stack = [root]
        res = ""
        visited = set()
        while stack:
            top = stack[-1]
            if top in visited:
                stack.pop()
                res += ")"
            else:
                visited.add(top)
                res += "(" + str(top.val)
                if not top.left and top.right:
                    res += "()"
                if top.right:
                    stack.append(top.right)
                if top.left:
                    stack.append(top.left)
        return res[1:-1]  # remove extra (): "(1(2(4))(3))"



