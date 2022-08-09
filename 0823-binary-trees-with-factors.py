"""
Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make. The answer may be too large so return the answer modulo 10^9 + 7.

Input: arr = [2,4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]

Input: arr = [2,4,5,10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
"""

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        # dp[i] =  ways to have a root node with value arr[i]
        # chilren must be smaller than the parent
        # if parent == left * right, then dp[p] += dp[l]*dp[r]
        dp = [1] * len(arr)
        MOD = 10**9 + 7
        arrSet = set(arr)
        arr = sorted(arr, reverse = True)
        idxMap = {}
        for i, v in enumerate(arr):
            idxMap[v] = i
            
        for i in range(len(arr)-2,-1,-1):
            for j in range(i+1, len(arr)):
                if arr[i] % arr[j] == 0:  # left
                    right = arr[i] // arr[j]
                    if right in arrSet:
                        dp[i] += dp[j] * dp[idxMap[right]]
                        dp[i] %= MOD
                        # print("dp->", dp)
        return sum(dp) % MOD
                    
       
            
                    