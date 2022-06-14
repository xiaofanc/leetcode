"""
split nums into 2 subsets with equal sum
solution: check if exists sum(subset) == target
"""

class Solution:
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

if __name__ == '__main__':
	s = Solution()
	print(s.canPartition([1,2,3,5])) # False
	print(s.canPartition([1,5,11,5])) # True





            
