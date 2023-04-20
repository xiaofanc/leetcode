"""
6138.
You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following conditions are satisfied:

t is a subsequence of the string s.
The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.
Return the length of the longest ideal string.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Note that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of 'a' and 'z' is 25, not 1.

Explanation
dp[c] means the length of the longest ideal subsequence
ending with character c.

Iterate the character i in string s,
c can be the next character for string ending from i - k to i + k.
So that dp[i] = max(dp[i-k], dp[i-k+1] ... , dp[i+k]) + 1.

return the max(dp) as result.
"""

class Solution:
    # TLE 69 / 84 test cases passed.
    def longestIdealString(self, s: str, k: int) -> int:
        if not s:
            return 0
        # L[i] = the longest ideal substring ends with s[i]
        
        L = [1] * len(s)
        maxL = 1
        for i in range(1, len(s)):
            for j in range(i):
                if abs(ord(s[j])-ord(s[i])) <= k and L[j]+1 > L[i]:
                    L[i] = L[j]+1
                if L[i] > maxL:
                    maxL = L[i]
        return maxL


    def longestIdealString(self, s: str, k: int) -> int:
        if not s:
            return 0
        # dp[i] = the longest ideal substring ends with char
        
        dp = [0] * 26
        for c in s:
            i = ord(c) - ord('a')
            dp[i] = max(dp[max(0,i-k):min(25,i+k)+1]) + 1
        return max(dp)

if __name__ == '__main__':
    s = Solution()
    print(s.longestIdealString("acfgbd", 2)) # 4 -> "acbd"




