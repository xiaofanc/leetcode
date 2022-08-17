# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(r: TreeNode) -> List[int]:
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        
        def find_two_swapped(nums: List[int]) -> (int, int):
            return [i for i,j in zip(nums, sorted(nums)) if i!= j]
        
        def findnode(node, target):
            if node == None: return node
            if node.val == target: return node
            return findnode(node.left, target) or findnode(node.right, target)
        
        x, y = find_two_swapped(inorder(root))
        nx, ny = findnode(root, x), findnode(root, y)
        nx.val, ny.val = ny.val, nx.val

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = x = y = None
        def inorder(node):
            nonlocal prev, x, y
            if not node:
                return
            inorder(node.left)
            if prev and node.val < prev.val:
                y = node     # find the last small number 
                if x is None:
                    x = prev # find the first large number
                else:
                    return
            prev = node
            inorder(node.right)
        inorder(root)
        x.val, y.val = y.val, x.val

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        cur = root
        prev = None
        large = small = None
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            else:
                node = stack.pop()
                if prev and node.val < prev.val:
                    # it is possible that small and large is not connected
                    # find the smallest node - which could be current root or
                    # a smaller number from right subtree
                    small = node
                    # find the first large number
                    if not large:
                        large = prev
                prev = node
                cur = node.right
        small.val, large.val = large.val, small.val

if __name__ == '__main__':
    s = Solution()
    print(s.recoverTree([1,3,null,null,2]))