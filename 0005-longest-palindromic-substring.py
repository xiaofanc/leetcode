class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == None or len(s) == 0: return ''
        start, end, maxlen = 0, 0, 0
        def expand(l, r):         # start from mid
            while l >= 0 and r < len(s) and s[l]==s[r]:
                l -= 1; r += 1
            return l+1, r-1

        for i in range(len(s)):
            l, r = expand(i, i)   # odd number
            if r - l > maxlen:
                start, end, maxlen = l, r, r-l
            l, r = expand(i, i+1) # even number
            if r - l > maxlen:
                start, end, maxlen = l, r, r-l
        return s[start:end+1]

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def expand(lo, hi):
            while lo >= 0 and hi < n and s[lo] == s[hi]:
                lo -= 1
                hi += 1
            return s[lo+1: hi]
        # if sequence is empty when picking up the max, then return default ""
        odd =  max((expand(i,i) for i in range(n)),      key = len, default = "")
        even = max((expand(i, i+1) for i in range(n-1)), key = len, default = "")
        return odd if len(odd) > len(even) else even

if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("babad"))