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

if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("babad"))