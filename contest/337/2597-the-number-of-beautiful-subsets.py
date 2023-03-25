"""
You are given an array nums of positive integers and a positive integer k.

A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

Input: nums = [2,4,6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].

"""
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        nums.sort()
        visited = set()
        res = 0
        n = len(nums)
        
        def subsets(start, comb):
            nonlocal res
            res += 1
            for i in range(start, n):
                if nums[i]-k not in comb:
                    comb.append(nums[i])
                    subsets(i+1, comb)
                    comb.pop()
                else:
                    continue
        subsets(0, [])
        return res-1
                
            
            