# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def traverse(subnums):
            if not subnums:
                return None
            else:
                max_node = max(subnums)
                i = subnums.index(max_node)
                n = TreeNode(max_node)
                n.left  = traverse(subnums[:i])
                n.right = traverse(subnums[i+1:])
                return n
        return traverse(nums)
        
if __name__ == '__main__':
    s = Solution()
    print(s.constructMaximumBinaryTree([3,2,1,6,0,5]))