"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

solution:
- we want all characters in a particular window to match the most common character in that window
- use two pointers for the window
- if windowlen - max(count.values()) <= k: valid window, then shift right pointer
- else: shift left pointer until valid
- res = longest valid window 
"""

class Solution:
	# Time: O(26n)
    def characterReplacement(self, s: str, k: int) -> int:
        res = l = 0
        count = {}
        for r in range(len(s)):
            char = s[r]
            count[char] = count.get(char, 0) + 1
            # if window is not valid, move left pointer
            while r-l+1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res
                
    # Time: O(n)
    def characterReplacement(self, s: str, k: int) -> int:
        res = l = 0
        count = {}
        maxf = 0
        for r in range(len(s)):
            char = s[r]
            count[char] = count.get(char, 0) + 1
            maxf = max(maxf, count[char])
            # check if window is valid
            # why we do not need to update maxf when l += 1?
            # since it will not change the res
            while r-l+1 - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res

if __name__ == '__main__':
	s = Solution()
	print(s.characterReplacement("AABABBA", 1))  # 4


