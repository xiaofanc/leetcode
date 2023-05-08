

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        count = 0
        res = 0
        l = r = 0
        while r < len(s):
            if s[r] in vowels:
                count += 1
            if r-l+1 > k:
                if s[l] in vowels:
                    count -= 1
                l += 1
            r += 1
            res = max(res, count)
        return res


            
