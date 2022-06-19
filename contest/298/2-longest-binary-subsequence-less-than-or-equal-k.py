"""
You are given a binary string s and a positive integer k.
Return the length of the longest subsequence of s that makes up a binary number less than or equal to k.

Input: s = "1001010", k = 5
Output: 5
Explanation: The longest subsequence of s that makes up a binary number less than or equal to 5 is "00010", as this number is equal to 2 in decimal.
Note that "00100" and "00101" are also possible, which are equal to 4 and 5 in decimal, respectively.
The length of this subsequence is 5, so 5 is returned.
"""
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        # start from right, including all 0s and include 1 if binary <= k, else break
        # count the 1 that can be included
        right = len(s)-1
        res = 0
        while right >= 0:
            if int(s[right:], 2) <= k:
                right -= 1
                res += 1
            else:
                break
        # count 0 before the current 1
        for i in range(right):
            if s[i] == '0':
                res += 1
        return res

        
