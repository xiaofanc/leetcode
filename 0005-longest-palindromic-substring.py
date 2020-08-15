"""
create a helper function which can expand from the center. If the left string equal 
to the right string and the pointers are sill in the range, then we move the left pointer
to the left, and move the right pointer to the right

and in the main function, we use for loop to check the longestpalindrome for each string
Also, there are two ways to expand, we can expand from center or expand from 
2 strings in the center

"""
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
        # if sequence is "a" when picking up the max, then even will not run, return default ""
        odd =  max((expand(i,i) for i in range(n)),      key = len, default = "")
        even = max((expand(i, i+1) for i in range(n-1)), key = len, default = "")
        return odd if len(odd) > len(even) else even

    def longestPalindrome(self, s: str) -> str:
            if len(s) == 0 or not s:
                return ""
            def expand(lo, hi):
                while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                    lo -= 1
                    hi += 1 
                return s[lo+1: hi]
            
            odd, even = "", ""
            for i in range(len(s)):
                if len(expand(i,i)) > len(odd):
                    odd = expand(i,i)
            for j in range(len(s)-1):
                if len(expand(j,j+1)) > len(even):
                    even = expand(j, j+1)
                    
            return odd if len(odd) > len(even) else even

    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        
        def expand(l, r):
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                l -= 1
                r += 1
                #print(l, r, s[l+1:r])
            return s[l+1:r]
        
        maxstr = ''
        for i in range(len(s)):
            #print(i)
            opt1 = expand(i, i)
            if len(opt1) > len(maxstr): 
                maxstr = opt1
                #print(opt1)
            opt2 = expand(i, i+1)
            if len(opt2) > len(maxstr):
                maxstr = opt2
                #print(opt2)
        return maxstr
                
            
                
if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("babad"))