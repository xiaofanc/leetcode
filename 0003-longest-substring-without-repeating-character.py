class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, lo, hi = 0, 0, 0
        charidx = {}
        for hi in range(len(s)):
            shi = s[hi]
            if shi in charidx:
                lo = max(lo, charidx[shi])
            ans = max(ans, hi-lo+1)
            charidx[shi] = hi+1
        return ans

    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, lo, hi = 0, 0, 0
        charidx = {}
        for hi in range(len(s)):
            if s[hi] in charidx and lo <= charidx[s[hi]]: # shi show again
                lo = charidx[s[hi]] + 1  # cut off the previous occurrence 
            else:
                ans = max(ans, hi-lo+1)
            charidx[s[hi]] = hi
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb") == 3)