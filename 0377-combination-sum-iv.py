"""
find all combinations (not unique)
The order of elements in the combination does matter for this problem.
num can be used multiple times

Given the target=4 and the candidates array nums=[1, 2, 3], each candidate number potentially can be the last number in the final combination. Here are a few steps on how we can work out a subset of valid combinations.

1). Suppose we place the number 1 as the last number in the combinations. Now, the remainder would be 4-1=3. We just reduce the problem into a smaller scale, where we should now find all the combinations that sum up to 3 rather than 4.

2). Suppose that we know the combinations that sum up to 3, which are [1, 1, 1], [1, 2] and [2, 1].

3). Now by appending the last number that we chose before (i.e. 1) to each of the above sub-combinations, we can now obtain all the valid and final combinations that end with the chosen number (i.e. [1, 1, 1, 1], [1, 2, 1], and [2, 1, 1]).

Now if we apply the above steps to each of the candidate numbers in the input array recursively, we could then obtain all subsets of combinations that end with each of the candidate numbers.

We could also prove that the combinations built with the above process are complete and non-redundant.

322. coin change: minimum number of coins that you need to make up target.
518. coin change: The number of combinations that make up that amount. [1,2] and [2,1] are the same, order does not matter.
"""

class Solution:
	# TLE: 8/15 test cases passed.
	# Time: O(N^T), space: O(T)
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = []
        def backtrack(i, left, comb):
            if left == 0:
                res.append(comb[:])
                return
            if left < 0:
                return
            for j in range(len(nums)):
                comb.append(nums[j])
                backtrack(j, left-nums[j], comb)
                comb.pop()
        backtrack(0, target, [])
        return len(res)

    # Top-down DP: Time: O(TxN), space: O(T)
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = []
        nums.sort()
        
        dp = {}
        def dfs(left):
            if left == 0:
                return 1
            
            if left in dp:
                return dp[left]
            res = 0
            for n in nums:
                if left >= n:
                    res += dfs(left-n)
                else:
                    break
            dp[left] = res
            return res
            
        return dfs(target)

    # bottom-up DP
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        # the value is set artificially to facilitate the calculation later 
        dp[0] = 1

        # how many ways to create i using all coins
        for i in range(target+1):
            for n in nums:
                if i >= n:
                    dp[i] += dp[i-n]
                    # print("dp->", dp)
        return dp[target]

if __name__ == '__main__':
	s = Solution()
	print(s.combinationSum4([1,2,3], 4)) # 7

	"""
	The possible combination ways are:
	(1, 1, 1, 1)
	(1, 1, 2)
	(1, 2, 1)
	(1, 3)
	(2, 1, 1)
	(2, 2)
	(3, 1)
	Note that different sequences are counted as different combinations.
	"""
