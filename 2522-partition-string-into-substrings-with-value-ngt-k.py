"""
You are given a string s consisting of digits from 1 to 9 and an integer k.

A partition of a string s is called good if:

Each digit of s is part of exactly one substring.
The value of each substring is less than or equal to k.
Return the minimum number of substrings in a good partition of s. If no good partition of s exists, return -1.

Input: s = "165462", k = 60
Output: 4
Explanation: We can partition the string into substrings "16", "54", "6", and "2". Each substring has a value less than or equal to k = 60.
It can be shown that we cannot partition the string into less than 4 substrings.

Input: s = "238182", k = 5
Output: -1
Explanation: There is no good partition for this string.
"""

class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        parts = []
        def partition(i, cur):
            if i == len(s):
                parts.append(cur)
                return True
            if cur*10 + int(s[i]) <= k:
                cur = cur*10 + int(s[i])
                if not partition(i+1, cur):
                    return False
            else:
                if cur != 0:
                    parts.append(cur)
                    if not partition(i, 0):
                        return False
                else:
                    return False
            return True
        return len(parts) if partition(0, 0) else -1
            
            