from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        strs.sort()
        print(strs)

        p = ""
        for x, y in zip(strs[0], strs[-1]):
            print(list(zip(strs[0], strs[-1])))
            if x == y: p += x
            else: break
        return p

s=Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))