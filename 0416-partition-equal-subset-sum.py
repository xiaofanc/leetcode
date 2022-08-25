"""
split nums into 2 subsets with equal sum
solution: check if exists sum(subset) == target

# 0698. canPartitionKSubsets
"""

class Solution:
    # TLE
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums)/2
        def backtracking(i, s):
            # print("s", s)
            if s == target:
                return True
            if s > target:
                return
            for j in range(i, len(nums)):
                s += nums[i]
                if backtracking(j+1, s): 
                    return True
                s -= nums[i]
        res = backtracking(0, 0)
        return True if res else False

	# DP
	# Time: O(n*sum(nums)), space: O(sum(nums))
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)/2 != sum(nums)//2:
            return False
        target = sum(nums)/2
        dp = set() # store subset sum
        dp.add(0)
        for n in nums:
            nextDP = set()
            for t in dp:
                nextDP.add(t)
                nextDP.add(t+n)
                if target in nextDP:
                    return True
            dp = nextDP
        return False

    # Time: O(mxn), where n be the number of array elements and m be the target
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums)/2
        nums.sort(reverse = True)
        memo = {}
        def backtrack(i, s):
            # if there is subsets from nums[i:] to make up to s
            if s == 0:
                return True
            if s < 0 or i == len(nums):
                return False
            if (i, s) in memo:
                return memo[(i, s)]
            # if no memoization: Time is O(2^n)
            res = backtrack(i+1, s-nums[i]) or backtrack(i+1, s)
            memo[(i, s)] = res
            return res

        return backtrack(0, target)



if __name__ == '__main__':
	s = Solution()
	print(s.canPartition([1,2,3,5])) # False
	print(s.canPartition([1,5,11,5])) # True





            
