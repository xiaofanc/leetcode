"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Time: O(N⋅2^N)
This is the worst-case time complexity when all the possible substrings are palindrome.
Detailed explanation of runtime complexity:
https://leetcode.com/problems/palindrome-partitioning/solution/
In general a string of length N will have N-1C0 + N-1C1 + ... +N-1CN-1 = O(2^N) partitionings.

Space: O(N)
store recursion stack
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def ispalindrome(s):
            l, r = 0, len(s)-1
            while l <= r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        def backtrack(i, comb):
            if i == len(s):
                res.append(comb[:])
                return
            for j in range(i, len(s)):
                if ispalindrome(s[i:j+1]):
                    comb.append(s[i:j+1])
                    backtrack(j+1, comb)
                    comb.pop()
        backtrack(0, [])
        return res

    # backtracking with DP
    def partition(self, s: str) -> List[List[str]]:
        # dp: determine if a substring starting at index start and ending at index end is a palindrome or not
        l = len(s)
        dp = [[False for i in range(l)] for j in range(l)]
        
        res = []
        def dfs(start, comb):
            if start >= l:
                res.append(comb[:])
            for end in range(start, l):
                if s[start] == s[end] and (end-start <= 2 or dp[start+1][end-1]):
                    dp[start][end] = True  # memoization
                    comb.append(s[start:end+1])
                    dfs(end+1, comb)
                    comb.pop()
        dfs(0, [])
        return res
                    
if __name__ == '__main__':
	s = Solution()
	print(s.partition("aabaa")) 
	# [["a","a","b","a","a"],["a","a","b","aa"],["a","aba","a"],["aa","b","a","a"],["aa","b","aa"],["aabaa"]]



