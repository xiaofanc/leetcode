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

if __name__ == '__main__':
    s = Solution()
    print(s.recoverTree([1,3,null,null,2]))