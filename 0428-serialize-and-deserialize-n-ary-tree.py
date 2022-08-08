"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        res = []
        def dfs(node):
            nonlocal res
            if not node:
                return
            res.append(str(node.val))
            for child in node.children:
                dfs(child)
            res.append("N") # mark - no more children
        dfs(root)
        return "#".join(res)
                
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return
        lst = [s for s in data.split("#") if s]
        root = Node(int(lst[0]), [])           # get the root first
        lst.pop(0)
        # print("lst->", lst)
        def dfs(node):
            if not lst:
                return
            while lst[0] != "N":               # to append each child for the node
                child = Node(int(lst[0]), [])  # [] for children
                node.children.append(child)
                lst.pop(0)
                dfs(child)                     # go deepers
            else:
                lst.pop(0)
                return       # return back to last level to add other children
        dfs(root)
        return root
        
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


