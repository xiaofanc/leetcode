import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scount = collections.Counter(s)
        tcount = collections.Counter(t)
        return scount == tcount
    
    def isAnagram(self, s: str, t: str) -> bool:
        dct = {}
        for l in s:
            dct[l] = dct.get(l, 0) + 1
        for l in t:
            dct[l] = dct.get(l, 0) - 1
        for k, v in dct.items():
            if v != 0:
                return False
        return True

s=Solution()
print(s.isAnagram("anagram","nagaram"))