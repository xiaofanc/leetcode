"""
find all non-overlapping palindromic substring with length >= k 
"""
class Solution:
	# does not satisfy non-overlapping
    def maxPalindromes(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i+k-1, len(s)):
                l, r = i, j
                while l < r:
                    if s[l] != s[r]:
                        break
                    else:
                        l += 1
                        r -= 1
                if l >= r:
                    res += 1
        return res

"""
https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/solutions/2808845/python3-dp-with-explanations-only-check-substrings-of-length-k-and-k-1/
https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/solutions/2809337/python-c-recursive-iterative-dp-solutions-explained/
"""
class Solution:
	# expand from center
    def maxPalindromes(self, s: str, k: int) -> int:
        res = 0
        lastp = -1

        def helper(l, r):
            nonlocal lastp, res
            while l >= 0 and r < len(s) and s[l] == s[r] and l > lastp:
                if r-l+1 >= k:
                    res += 1
                    lastp = r
                    break # find the shortest palindrome
                else:
                    l -= 1
                    r += 1
        
        for i in range(len(s)):
            helper(i, i)  # odd length
            helper(i, i+1)  # even length
        return res

