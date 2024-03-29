"""
Think of it as moving back up in the tree to explore the next branch. When we moved down of one level, we swapped 2 elements (1st swap in the code). So when we go back up in the tree we need to swap these 2 elements back to their original order at the parent node level (2nd swap in the code). This is called backtracking = done exploring a branch, let's go back up and explore more branches.

Time: O(N x N!)
since you will have N! permutation. And, for each permutation, you run exact N recursive call to reach it. So it should be N x N! 

Space: O(N)
N! solutions.

nums[:]
# it is a deep copy. nums refers to the same address, and every time a permutation is there, need to copy the current nums, and backtracking will modify the nums in the same address
"""


class Solution:
    # Time: partial permutation - sum_{k=1}_n (n!/(n-k!))
    # Space: O(n)
    def permute(self, nums: List[int]) -> List[List[int]]:
      
        def backtrack(i = 0):
            # base case: if all integers are used up
            if i == n:
                output.append(nums[:]) # deep copy num
            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i + 1)
                # return to the parent node 
                nums[i], nums[j] = nums[j], nums[i]
        
        n = len(nums)
        output = []
        backtrack()
        return output

if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3])) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,2,1],[3,1,2]]




    