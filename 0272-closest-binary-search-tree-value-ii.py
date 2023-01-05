# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time: O(nlogk)
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        maxHeap = [] # key is the dist
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            dist = abs(target-root.val)
            heapq.heappush(maxHeap, (-dist, root.val))
            if len(maxHeap) > k:  # keep the size == k
                heapq.heappop(maxHeap)

            # early stop since values will be larger in BST inoder traversal
            if dist > -heap[0][0]:
                return
                
            inorder(root.right)
        inorder(root)
        return [val[1] for val in maxHeap]

if __name__ == '__main__':
    s = Solution()
    print(s.closestKValues([4,2,5,1,3], 3.714286, k))

