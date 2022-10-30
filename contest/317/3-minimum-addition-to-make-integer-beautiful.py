
class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        # 123456 -> 123460 -> 123500 -> 124000 -> 130000 -> 200000
        n0 = n
        i = 0 # count 0
        # digits = [int(i) for i in str(n)]
        while sum(map(int, str(n))) > target:
            n = n // 10 + 1
            i += 1
        return n*(10**i)-n0
            
        