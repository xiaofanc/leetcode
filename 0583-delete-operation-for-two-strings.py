"""
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
In one step, you can delete exactly one character in either string.
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def helper(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(word1):
                return len(word2[j:])
            if j == len(word2):
                return len(word1[i:])
            d = len(word1) + len(word2)
            if word1[i] == word2[j]:
                d = min(d, helper(i+1, j+1))
            else:
                d = min(d, 1 + min(helper(i+1, j), helper(i, j+1)))
            memo[(i, j)] = d
            return d
        
        return helper(0, 0)
        
if __name__ == '__main__':
    s = Solution()
    print(s.minDistance("sea", "aet"))



