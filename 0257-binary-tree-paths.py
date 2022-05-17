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

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(node):
            if not node: return []
            ans = []
            if not node.left and not node.right:
                ans.append(str(node.val))
            if node.left:
                for l in dfs(node.left):
                    ans.append(str(node.val) + "->" + l)
            if node.right:
                for r in dfs(node.right):
                    ans.append(str(node.val) + "->" + r)
            return ans
        return dfs(root)

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        res = []
        def backtrack(node, path):
            path.append(node.val)
            if not node.left and not node.right:
                path = [str(c) for c in path]
                res.append('->'.join(path))
                return
            if node.left: 
                backtrack(node.left, path)
                path.pop()
            if node.right:
                backtrack(node.right, path)
                path.pop()               
                
        backtrack(root, [])
        return res

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        res = []
        def dfs(node, path):
            path += str(node.val)
            if not node.left and not node.right:
                res.append(path)
                return
            if node.left: 
                dfs(node.left, path + "->") 
                # why no backtracking?
            if node.right:
                dfs(node.right, path + "->")
                
        dfs(root, "")
        return res

if __name__ == '__main__':
    T = TreeNode
    t1 = T(1, T(2, T(4), T(5)), T(3))
    print(t1)
   
    s=Solution()
    print(s.binaryTreePaths0(t1)) # ["1->3","1->2->5","1->2->4"]
    print(s.binaryTreePaths1(t1))    
