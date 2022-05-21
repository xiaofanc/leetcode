513. find bottom left value from a tree

def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
    maxdepth, leftmostvalue = -float("inf"), 0
    def traversal(node, depth):
        # 全局变量
        nonlocal maxdepth, leftmostvalue
        if not node.left and not node.right:
            if depth > maxdepth:
                maxdepth = depth
                leftmostvalue = node.val
        if node.left:
            depth += 1
            traversal(node.left, depth)  # traversal(node.left, depth+1)
            depth -= 1
        if node.right:
            depth += 1
            traversal(node.right, depth)
            depth -= 1
    traversal(root, 0)
    return leftmostvalue