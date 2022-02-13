# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
            

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # DFS preorder transversal
        def preorder(root, string):
            if not root:
                string += 'None,'
            else:
                string += str(root.val) + ","
                string = preorder(root.left, string)
                string = preorder(root.right, string)
            return string
        return preorder(root, "")

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def rdeserialize(data):
            if data[0] == 'None':
                data.pop(0)
                return None
            
            root = TreeNode(data[0])
            data.pop(0)
            root.left = rdeserialize(data)
            root.right = rdeserialize(data)
            return root
        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))