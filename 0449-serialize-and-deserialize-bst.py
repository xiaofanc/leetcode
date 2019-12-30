# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        vals = []
        # preorder so that the root in always in the front
        def preorder(node):
            if not node: return None
            else:
                vals.append(node.val)
                preorder(node.left)
                preorder(node.right)
            return vals
        preorder(root)
        return " ".join(map(str, vals)) # tranform each node in list into str
        
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        q = deque(int(i) for i in data.split())
        def build(minval, maxval):
            if q and  minval < q[0] < maxval:
                pivot = q.popleft()
                node = TreeNode(pivot)
                node.left  = build(minval, pivot)
                node.right = build(pivot, maxval)
                return node
        return build(float("-inf"), float("inf"))



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))