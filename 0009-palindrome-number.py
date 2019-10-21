class Solution:
    def isPalindrome(self, x):

        #solution1
        if x < 0:
            return False
        if 0 <= x < 10:
            return True
        left = 0
        right = len(str(x)) - 1
        while left < right:
            if str(x)[left] != str(x)[right]: 
                return False
            left += 1
            right -= 1
        return True
        
        # solution2
        s = str(x)
        return s == s[::-1]
        
        #solution3
        return False if x < 0 else x == int(str(x)[::-1])