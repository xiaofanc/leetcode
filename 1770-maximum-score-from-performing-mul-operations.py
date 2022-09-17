"""
Greedy does not work.
We cannot pick the larger one between nums[l] and nums[r] to get the maximum results since multipliers is not in ascending order.
example:
nums = [5,1,3], multipliers = [3,4,1]
5*3+3*4+1*1 = 28
3*3+4*5+1*1 = 30

Two options for each multipliers[i]:
nums[l]*multipliers[i]+dfs(i+1, l+1, r)
nums[r]*multipliers[i]+dfs(i+1, l, r-1)

Hence, there are 3 state variables, left, right, and op. Thus, it's a 3D Dynamic Programming problem. And to memoize it, we may need a 3D array.
However, with mathematics, we can reduce these 3 state variables to 2. 

The right is related to op, left and len(nums)=n as:
left + (n-right-1) = op
right = n-1-op+left

Therefore, we can define a state with only two state variables op and left.
dp[op][left] stores the maximum possible score after we finish m operations using any left numbers from the current state.

If op != m, we have two options:
- select left: we will multiply mulitpliers[op] and nums[left] and add this product to (optimal) result of state dp[op+1][left+1].

- select right: we will multiply mulitpliers[op] and nums[right] and add this product to (optimal) result of state dp[op+1][left].

If op == m, means we have performed m operations, add 0. The base Condition of Recursion.

Create a 2D array dp of size m+1 by m+1. Reason being op can vary from 0 to m, and so does left.
# op should start from end since we need to know dp[op+1][left+1] to calculate dp[op][left]
for op in range(m-1,-1,-1): 
    # left at most move op steps
    for left in range(op-1,-1,-1):

I have 2 questions for this problem:
Q1. Why iterate over left from op to 0 for each op?
Q2. What is the meaning of `dp[0][0]`?
"""
class Solution:
    # TLE: O(2^M)
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # to determine a state, we need l, r and i
        memo = {}
        def dfs(i, l, r):
            if (i, l) in memo:
                return memo[(i, l)]
            if l > r or l == len(nums) or r == -1 or i == len(multipliers):
                return 0
            memo[(i, l)] = max(nums[l]*multipliers[i]+dfs(i+1, l+1, r), nums[r]*multipliers[i]+dfs(i+1, l, r-1))
            return memo[(i, l)]
        return dfs(0, 0, len(nums)-1)

    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # constraint: n >= m >= 1
        # Number of Operations
        m = len(multipliers)

        # For Right Pointer
        n = len(nums)

        dp = [[0] * (m + 1) for _ in range(m + 1)]

        for op in range(m - 1, -1, -1):
            for left in range(op, -1, -1):

                dp[op][left] = max(multipliers[op] * nums[left] + dp[op + 1][left + 1],
                                   multipliers[op] * nums[n - 1 - (op - left)] + dp[op + 1][left])

        return dp[0][0]

if __name__ == '__main__':
     s = Solution()
     print(s.maximumScore([1,2,3], [1,3,2]))  # 14



