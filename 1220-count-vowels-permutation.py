"""
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

"""

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[1,1,1,1,1] for i in range(n)]
        MOD = 10**9+7
        for i in range(1,n):
        	# end with 'a'
            dp[i][0] = (dp[i-1][1] + dp[i-1][2] + dp[i-1][4]) % MOD
            # end with 'e'
            dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD
            # end with 'i'
            dp[i][2] = (dp[i-1][1] + dp[i-1][3]) % MOD
            # end with 'o'
            dp[i][3] = (dp[i-1][2]) % MOD
            # end with 'u'
            dp[i][4] = (dp[i-1][2] + dp[i-1][3]) % MOD
        return sum(dp[n-1]) % MOD

if __name__ == '__main__':
	s = Solution()
	print(s.countVowelPermutation(1))
	print(s.countVowelPermutation(2))


	