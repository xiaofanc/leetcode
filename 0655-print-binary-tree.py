

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:

        def getHeight(node):
            if not node:
                return -1
            return 1+max(getHeight(node.left), getHeight(node.right))

        h = getHeight(root)
        r, c = h+1, 2**(h+1)-1
        res = [[""]*c for i in range(r)]

        def populate(node, r, c):
            if not node:
                return
            res[r][c] += str(node.val)
            populate(node.left, r+1, c-2**(h-r-1))
            populate(node.right, r+1, c+2**(h-r-1))

        populate(root, 0, (c-1)//2)
        return res