class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def sgen(node):
            if node:
                yield str(node.val)
                yield from sgen(node.left)
                yield from sgen(node.right)
            else:
                yield "#"
        return ",".join(sgen(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dgen(vals):
            val = next(vals)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = dgen(vals)
            node.right = dgen(vals)
            return node
        return dgen(iter(data.split(",")))


class Solution:

        # generator
        def levelOrder2(self, root):
            level = [root]
            while level:
                yield [node.val for node in level]
                level = [child for node in level for child in [node.left, node.right] if child]

if __name__ == '__main__':
    s = Solution()
    T = TreeNode
    root = T(1, T(2, T(4)), T(3, T(5, T(7)), T(6)))
    # print(s.levelOrder(root))
    g = s.levelOrder2(root)
    print(next(g))
    print(next(g))
    print(next(g))


