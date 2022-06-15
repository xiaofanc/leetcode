"""
Given two strings s and t, return the number of distinct subsequences of s which equals t.
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
|rabb|b|it|
|rab|b|bit|
|ra|b|bbit|

if s[i] == t[j]: check (i+1, j+1) -> does not mean next (i+1) could not match
Therefore, check (i+1, j) as well
else: check (i+1, j) why? we need to match t

base case: s = "", t = "" => return 1
		   s = "abv", t = "" => return 1
		   s = "", t = "abd" => return 0
"""

class Solution:
	# Time = space = O(MxN)
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        m, n = len(s), len(t)
        def dfs(i, j):
            if i == m and j == n: # s = "", t = "" 
                return 1
            elif i == m:  # s = "", t = "abd"
                return 0
            elif j == n:  # s = "abv", t = ""
                return 1
            elif (i,j) in dp:
                return dp[(i,j)]
            else:
                if s[i] == t[j]: 
                	# move both pointers or move only i pointer
                    dp[(i, j)] = dfs(i+1, j+1) + dfs(i+1, j)
                else:
                	# move only i pointer to match j
                    dp[(i, j)] = dfs(i+1, j)
            return dp[(i, j)]
        return dfs(0, 0)

if __name__ == '__main__':
	s = Solution()
	print(s.numDistinct("rabbbit", "rabbit")) # 3





