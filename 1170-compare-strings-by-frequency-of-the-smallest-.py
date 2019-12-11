import bisect
from typing import List

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            return s.count(min(s))
        def bs(l, target):
            lo, hi = 0, len(l)
            #print(l, target)
            while lo < hi:
                #print(lo, hi, mid)
                mid = (lo+hi)//2
                if l[mid] > target:
                    hi = mid
                else:
                    lo = mid+1
            return lo

        freqw = sorted(f(w) for w in words)
        lenw = len(words)
        return [lenw - bs(freqw, f(query)) for query in queries]

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            return s.count(min(s))
        freqw = sorted(f(w) for w in words)
        lenw = len(words)
        return [lenw - bisect.bisect(freqw, f(query)) for query in queries]
        
if __name__ == '__main__':
    s = Solution()
    print(s.numSmallerByFrequency(["bbb","cc"],["a","aa","aaa","aaaa"]))
    print(s.numSmallerByFrequency(["bba","abaaaaaa","aaaaaa","bbabbabaab","aba","aa","baab","bbbbbb","aab","bbabbaabb"], ["aaabbb","aab","babbab","babbbb","b","bbbbbbbbab","a","bbbbbbbbbb","baaabbaab","aa"]))
    print(s.numSmallerByFrequency(["cbd"], ["zaaaz"]))

