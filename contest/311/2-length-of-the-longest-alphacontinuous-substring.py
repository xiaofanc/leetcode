"""
An alphabetical continuous string is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string "abcdefghijklmnopqrstuvwxyz".

For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not.
Given a string s consisting of lowercase letters only, return the length of the longest alphabetical continuous substring.
"""
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        res = 0
        l = r = 0
        while r < len(s):
            if r == 0 or (ord(s[r]) - ord(s[r-1]) == 1):
                res = max(r-l+1, res)
            else:
                l = r
            r += 1
        return res
                
                
                