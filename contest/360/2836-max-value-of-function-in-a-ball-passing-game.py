"""
better solution: binary lifying
"""
class Solution:
    # O(nk)
    # TLE: 909 / 947 test cases passed.
    # case: [0], 100000000
    def getMaxFunctionValue(self, r: List[int], k: int) -> int:
        res = 0
        seen = set()
        for i in range(len(r)):
            c = 0
            score = i
            nxt = i
            while c < k:
                score += r[nxt]
                c += 1
                nxt = r[nxt]
            res = max(res, score)
        return res