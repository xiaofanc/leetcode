
class Solution:
    def canConstruct(self, t: str, s: str) -> bool:
        dct = {}
        for l in s:
            dct[l] = dct.get(l, 0) + 1
        for l in t:
            dct[l] = dct.get(l, 0) - 1
        for k, v in dct.items():
            if v < 0:
                return False
        return True

s=Solution()
print(s.canConstruct("anagram","nagaram"))
print(s.canConstruct("aa","aab"))
