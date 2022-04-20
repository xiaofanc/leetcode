"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Time: O(N⋅2^N)
This is the worst-case time complexity when all the possible substrings are palindrome.

Space: O(N)
store recursion stack
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        def isPalindrome(start, end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        def dfs(start, path, x):
            # print("   "*x, start, path)
            if start >= n:
                res.append(path)
                return
            for i in range(start, n):
                if isPalindrome(start, i):
                	# check the remaining characters
                    dfs(i+1, path + [s[start:i+1]], x+1)
        dfs(0, [], 0)
        return res                

    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        def isPalindrome(start, end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        def backtrack(start, path, x):
            # print("   "*x, start, path)
            if start >= n:
                res.append(path[:])
                return
            for i in range(start, n):
                if isPalindrome(start, i):
                    path.append(s[start:i+1])
                    backtrack(i+1, path, x+1)
                    path.pop()
        backtrack(0, [], 0)
        return res

if __name__ == '__main__':
	s = Solution()
	print(s.partition("aabaa")) 
	# [["a","a","b","a","a"],["a","a","b","aa"],["a","aba","a"],["aa","b","a","a"],["aa","b","aa"],["aabaa"]]



