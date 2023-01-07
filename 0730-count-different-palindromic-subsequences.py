"""
DFS(start, end): represents the distinct palindrome subsequence in s[start:end]
- find the first (i) and last occurrence (j) of 'abcd'
- if we are looking at 'a'
- if i == j: There is only one 'a' in the segment. So the answer is 1.
- else: The possible palindrome could be 'a', 'aa', 'a*a', * could be possible palindrome in [i+1, j-1] (DFS(i+1, j-1))

Use cache to store DFS(start, end), inclusive start and end

s = "abccba"
dp[0,5] = a + b + c
        = (dp[1,4]+2) + (dp[2,3]+2) + (dp[3,2]+2)
        = (dp("bccb")+"a"+"aa") + (dp("cc")+"b"+"bb") + (dp("")+"c"+"cc")
        = ((b + c)+2) + ((c)+2) + 2
        = ((dp[2,3]+2 + dp[3,2]+2)+2) + (dp[3,2]+2+2) + 2
        = 0+2+2       + 0+2+2         + 0+2+2         + 2
        = 14
"""

class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        cache = {}
        def dfs(start, end): # inclusive
            if (start, end) in cache:
                return cache[(start, end)]
            
            cnt = 0
            segment = s[start:end+1]
            for x in 'abcd':
                try:
                    l = segment.index(x) + start
                    r = segment.rindex(x) + start
                except:
                    continue
                if l == r:
                    cnt += 1
                else:
                    cnt += dfs(l+1, r-1) + 2
            cache[(start, end)] = cnt
            return cnt % (10**9+7)
        return dfs(0, len(s)-1)
            
if __name__ == '__main__':
	s = Solution()
	print(s.countPalindromicSubsequences("abccba")) # 14
	print(s.countPalindromicSubsequences("bccb")) # 6 - 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'
    # 'b', 'bb', 'bcb', 'bccb'
    # 'c', 'cc'



	

