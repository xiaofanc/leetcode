from typing import List

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')


#iteration
class Solution:
    def binaryTreePaths0(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        
        paths = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))
        return paths

# recursion
    def binaryTreePaths1(self, root: TreeNode) -> List[str]:
        
        def construct_paths(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path += '->'
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)
                    
        paths = []
        construct_paths(root,'')
        return paths      

if __name__ == '__main__':
    T = TreeNode
    t1 = T(1, T(2,T(5)), T(3))
    print(t1)
   
    s=Solution()
    print(s.binaryTreePaths0(t1))
    print(s.binaryTreePaths1(t1))    
