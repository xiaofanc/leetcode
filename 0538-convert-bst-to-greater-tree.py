class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.total = 0
        def trans(node):
            if not node: return 0
            trans(node.right)
            self.total += node.val
            node.val = self.total
            trans(node.left)
        trans(root)
        return root
        

if __name__ == '__main__':
    s = Solution()
    print(s.convertBST([5,2,13]) == [18,20,13]) 
    print(s.convertBST([4,2,5,1,3]) == [9,14,5,15,12]) 
                
                
                
