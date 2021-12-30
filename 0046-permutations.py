"""
Think of it as moving back up in the tree to explore the next branch. When we moved down of one level, we swapped 2 elements (1st swap in the code). So when we go back up in the tree we need to swap these 2 elements back to their original order at the parent node level (2nd swap in the code). This is called backtracking = done exploring a branch, let's go back up and explore more branches.
"""


class Solution:
    # Time: partial permutation - sum_{k=1}_n (n!/(n-k!))
    # Space: O(n!)
    def permute(self, nums: List[int]) -> List[List[int]]:
      
        def backtrack(first = 0):
            # base case: if all integers are used up
            if first == n:
                output.append(nums[:]) # deep copy num
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                # return to the parent node 
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        output = []
        backtrack()
        return output

if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3])) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,2,1],[3,1,2]]




    