"""
The alternating sum of a 0-indexed array is defined as the sum of the elements at even indices minus the sum of the elements at odd indices.
For example, the alternating sum of [4,2,5,3] is (4 + 5) - (2 + 3) = 4.
Given an array nums, return the maximum alternating sum of any subsequence of nums (after reindexing the elements of the subsequence).

"""
class Solution:
	def maxAlternatingSum(self, nums: List[int]) -> int:
		# previous sum
	    sumEven, sumOdd = 0, 0

	    for i in range(len(nums)-1,-1,-1):
			# The first value of subsequence is even, include or not include
	        tmpEven = max(sumOdd+nums[i], sumEven)
			
			# The first value of subsequence is odd, include or not include
	        tmpOdd = max(sumEven-nums[i], sumOdd)

	        sumEven, sumOdd = tmpEven, tmpOdd
	    return sumEven

    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i, even):
            if i == len(nums):
                return 0
            if (i, even) in dp:
                return dp[(i, even)]
            total = nums[i] if even else -nums[i]
            # two decision, add the current value, skip the current value
            dp[(i,even)] = max(total+dfs(i+1, not even), dfs(i+1, even))
            return dp[(i,even)]
        return dfs(0, True)

if __name__ == '__main__':
	s = Solution()
	print(s.maxAlternatingSum([4,2,5,3])) # It is optimal to choose the subsequence [4,2,5] with alternating sum (4 + 5) - 2 = 7.
	print(s.maxAlternatingSum([5,6,7,8])) # It is optimal to choose the subsequence [8] with alternating sum 8.


