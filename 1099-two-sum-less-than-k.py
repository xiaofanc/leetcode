from typing import List

class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        a = sorted(A)
        i, j = 0, len(A)-1
        ans = -1
        while i < j:
            if a[i] + a[j] < K:
                ans = max(ans, a[i] + a[j])
                i += 1
            else:
                j -= 1
        return ans
            
            
if __name__ == '__main__':
    s = Solution()
    print(s.twoSumLessThanK([34,23,1,24,75,33,54,8], 60) == 58)
    print(s.twoSumLessThanK([10,20,30], 15) == -1)