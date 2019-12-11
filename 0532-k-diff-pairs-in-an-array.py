from typing import List
from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        if k == 0: return sum(1 for key in count if count[key] >1)
        if k > 0: return sum(1 for key in count if key-k in count)
        return 0
    
    def findPairs(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        res = 0
        for i in c:
            if (k > 0 and k+i in c) or (k == 0 and c[i] > 1):
                res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findPairs([3, 1, 4, 1, 5],2) == 2)
    print(s.findPairs([1, 2, 3, 4, 5],1) == 4)
    print(s.findPairs([1, 3, 1, 5, 4],0) == 1)