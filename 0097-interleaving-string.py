
class Solution:
	# TLE: 66/106 passed
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        def dfs(i, j, res):
            if i == len(s1) and j == len(s2) and res == s3:
                return True
            ans = False
            if i < len(s1):
                ans = ans or dfs(i+1, j, res+s1[i])
            if j < len(s2):
                ans = ans or dfs(i, j+1, res+s2[j])
            return ans

        if len(s1) + len(s2) != len(s3):
            return False
        return dfs(0, 0, "")


    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        def dfs(i, j, k):
            if (i, j) in memo:
                return memo[(i,j)]
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            if i == len(s1):
                return s2[j:] == s3[k:]
            if j == len(s2):
                return s1[i:] == s3[k:]
            ans = False
            if s1[i] == s3[k]:
                ans = ans or dfs(i+1, j, k+1)
            if s2[j] == s3[k]:
                ans = ans or dfs(i, j+1, k+1)
            memo[(i,j)] = ans
            return ans

        if len(s1) + len(s2) != len(s3):
            return False
        return dfs(0, 0, 0)
        