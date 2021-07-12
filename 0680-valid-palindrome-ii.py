class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        l, r = 0, len(s)-1
        
        while l < r:
            if s[l] != s[r]:
                return helper(s, l+1, r) or helper(s, l, r-1)
            l += 1
            r -= 1
        return True


    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #left, right = 0, len(s)-1
        #while left < right:
        #    if s[left] != s[right]:
        #        one, two = s[left:right], s[left+1:right+1]
        #        return one == one[::-1] or two == two[::-1]
        #    left += 1
        #    right -= 1
        #return True

        i, j = 0, len(s) - 1
        
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.validPalindromeUtil(s, i + 1, j) or self.validPalindromeUtil(s, i, j - 1)
        return True
    
    def validPalindromeUtil(self, s, i, j):
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.validPalindrome("abc"))



    