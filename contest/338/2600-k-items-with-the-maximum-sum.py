
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        res = 0
        res += min(k, numOnes)
        k -= numOnes
        k -= numZeros
        if k <= 0:
            return res
        return res-k