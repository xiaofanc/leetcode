#method1:
from itertools import groupby
from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = 0
        for c, group in groupby(chars):
            #print(c, len(list(group)))
            ans += 1
            print(ans)
            lengrp = len(list(group))
            print(lengrp)
            if lengrp > 1:
                ans += len(str(lengrp))
                print(ans)
        return ans

s=Solution()
#print(s.compress(["a","a","b","b","c","c","c","c","c","c","c","c","c","c","c","c"]))

class Solution:
    def compressd(self, chars: List[str]) -> int:
        ans = []
        for c, group in groupby(chars):
            #print(c, len(list(group)))
            ans.append(c)
            lengrp = len(list(group))
            if lengrp > 1:
                ans.extend(list(str(lengrp)))
                print(ans,str(lengrp),list(str(lengrp)))
        chars[:] = ans
        return len(ans)
            
s=Solution()
#print(s.compressd(["a","a","b","b","c","c","c","c","c","c","c","c","c","c","c","c"]))

#method2:
class Solution:
    def compress(self, chars: List[str]) -> int:
        # a is the start of group, k is the next position to be replaced
        a = k = 0
        for b, char in enumerate(chars):
            if b + 1 == len(chars) or chars[b+1] != char:
                chars[k] = chars[a]
                k += 1
                if b > a:
                    for digit in str(b - a + 1):
                        chars[k] = digit
                        k += 1
                # move to the next group
                a = b + 1
        return k

s=Solution()
print(s.compress(["a","a","b","b","c","c","c","c","c","c","c","c","c","c","c","c"]))