# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# pre order or level order

# DFS 
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
                string += 'None,'   # when to return when rebuilding the tree
            else:
                string += str(root.val) + ","   # in case of negative val
                string = preorder(root.left, string)
                string = preorder(root.right, string)
            return string
        return preorder(root, "")

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(lst, x):
            if lst[0] == "N":
                lst.pop(0)               # lst is changed in the recursion and changed when passing in right subtree recursion
                print(" "*x, lst)        # lst pop works like a global variable
                print(" "*x, "return")   # lst = lst[1:] does not work since slicing lists does not generate copies of the objects in the list; it just copies the references to it
                return None
            root = TreeNode(int(lst.pop(0)))
            print(" "*x, lst)
            root.left = helper(lst, x+1)  # x is a local variable, only change in the recursion
            root.right = helper(lst, x+1) # x passed in = previous x passed in
            return root
        return helper(data.split(","), 0)

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(root):
            nonlocal res
            if not root:
                res.append("N")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            # res is global variable, no need to return
        dfs(root)
        return ",".join(res)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        print("vals", vals)
        self.i = 0           # must be global variable
        
        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            root = TreeNode(int(vals[self.i]))
            self.i += 1
            # if pass i into dfs, i will not change if not return
            root.left = dfs()   
            root.right = dfs()
            return root
        return dfs()        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# BFS - level order
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # print("data->", data)
        lst = data.split(",")
        queue = deque()
        if lst[0] != "N":
            root = TreeNode(int(lst[0]))
            queue.append(root)
        else:
            return None
        i = 1
        while queue and i < len(lst):
            node = queue.popleft()
            if lst[i] != "N":
                left =  TreeNode(lst[i])
                node.left = left
                queue.append(left)
            i += 1                  # move to the next node
            if lst[i] != "N":
                right = TreeNode(lst[i])
                node.right = right
                queue.append(right)
            i += 1
        return root




