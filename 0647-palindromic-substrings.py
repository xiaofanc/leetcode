"""
Given a string s, return the number of palindromic substrings in it.
"""
class Solution:
    # Time: O(n^2)
    def countSubstrings(self, s: str) -> int:
        res = 0
        def helper(l, r):
            nonlocal res
            while l >= 0 and r <= len(s)-1 and s[l] == s[r] :
                res += 1
                l -= 1
                r += 1
        # loop over every position in s
        for i in range(len(s)):
        	# count the number of palindromes which use s[i] as the center - odd length
            helper(i, i)
            # count the number of palindromes which use s[i], s[i+1] as the center - even length
            helper(i, i+1)
        return res

    # Time: O(n^2)
    def countSubstrings(self, s: str) -> int:
        dp = [[False]*len(s) for _ in range(len(s))]
        res = 0
        for j in range(len(s)):
            for i in range(j+1):
                # single letter
                if i == j:
                    dp[i][j] = True
                    res += 1
                # double letter
                elif i + 1 == j:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        res += 1
                else:
                    dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                    res += dp[i][j]

        return res

if __name__ == '__main__':
	s = Solution()
	print(s.countSubstrings("aaa")) # 6 -> "a", "a", "a", "aa", "aa", "aaa"

