"""
DFS(start, end): represents the distinct palindrome subsequence in s[start:end]
- find the first (i) and last occurrence (j) of 'abcd'
- if we are looking at 'a'
- if i == j: There is only one 'a' in the segment. So the answer is 1.
- else: The possible palindrome could be 'a', 'aa', 'a*a', * could be possible palindrome in s[i+1, j] (DFS(i+1, j))

Use cache to store DFS(start, end)

s = "abccba"
dp[0,5] = dp[1,4]+2 + dp[2,3]+2
        = (dp[2,4]+2)+2 + dp[2,3]+2
        = (dp[3,4]+2+2)+2 + (dp[3,3]+2)+2
        = (dp[4,4]+2+2+2)+2 + (dp[3,3]+2)+2
        = (1+2+2+2)+2+(1+2)+2
        = 14
"""

class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        cache = {}
        def dfs(start, end): # return res for s[start:end]
            if (start, end) in cache:
                return cache[(start, end)]
            cnt = 0
            segment = s[start:end]
            for x in 'abcd':
                try: # 'a' not in 'bccb'
                    l = segment.index(x) + start
                    r = segment.rindex(x) + start
                except:
                    continue
                if l == r:
                    cnt += 1
                else: # get res for s[l+1:r]
                    cnt += dfs(l+1, r) + 2
            cache[(start, end)] = cnt
            return cnt % (10**9+7)
        return dfs(0, len(s))
            
                    
if __name__ == '__main__':
	s = Solution()
	print(s.countPalindromicSubsequences("abccba")) # 14
	print(s.countPalindromicSubsequences("bccb")) # 6 - 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'




	

