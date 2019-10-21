import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scount = collections.Counter(s)
        tcount = collections.Counter(t)
        return scount == tcount
            
s=Solution()
print(s.isAnagram("anagram","nagaram"))