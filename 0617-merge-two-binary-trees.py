class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')

class Solution:
    def mergeTrees(self, r1: TreeNode, r2: TreeNode) -> TreeNode:
        if r1 == None and r2 == None:
            return None
        elif r1 == None and r2 != None:
            return r2
        elif r2 == None and r1 != None:
            return r1
        else:
            node = TreeNode(r1.val + r2.val) 
            node.left = self.mergeTrees(r1.left, r2.left)
            node.right = self.mergeTrees(r1.right, r2.right)
            return node
    
    def mergeTrees(self, r1: TreeNode, r2: TreeNode) -> TreeNode:
        # reuse r1
        if r1 == None and r2 == None:
            return None
        elif r1 == None and r2 != None:
            return r2
        elif r2 == None and r1 != None:
            return r1
        else:
            r1.val = r1.val + r2.val
            r1.left = self.mergeTrees(r1.left, r2.left)
            r1.right = self.mergeTrees(r1.right, r2.right)
            return r1

    def mergeTrees(self, t1, t2):
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
            return root
        else:
            return t1 or t2

    # iterative, replace root1
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        que = deque()
        que.append(root1)
        que.append(root2)
        while que:
            node1, node2 = que.popleft(), que.popleft()
            node1.val += node2.val
            if node1.left and node2.left:
                que.append(node1.left)
                que.append(node2.left)
            if node1.right and node2.right:
                que.append(node1.right)
                que.append(node2.right)
            if not node1.left and node2.left:
                node1.left = node2.left
            if not node1.right and node2.right:
                node1.right = node2.right
        return root1

if __name__ == '__main__':
    T = TreeNode
    r1 = T(1, T(2), T(3,T(4)))
    r2 = T(1, T(2), T(3,T(4)))
    s = Solution()
    print(s.mergeTrees(r1, r2))          
        
            