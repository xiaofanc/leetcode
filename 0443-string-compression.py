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
        anchor = write = 0
        for read, c in enumerate(chars):
            print()
            print('line 43', chars, read, c)
            if read + 1 == len(chars) or chars[read+1] != c:
                chars[write] = chars[anchor]
                print('line 46',write, chars[write], anchor, chars[anchor])
                write += 1
                print('line 48',write, read, anchor)
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        print('line 51', str(read - anchor + 1))
                        chars[write] = digit
                        write += 1
                anchor = read + 1
                print('line 55', write, read, anchor)
        return write

s=Solution()
print(s.compress(["a","a","b","b","c","c","c","c","c","c","c","c","c","c","c","c"]))