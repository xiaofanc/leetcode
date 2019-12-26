class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        tn0, tn1, tn2 = 0, 1, 1
        for i in range(n-2):
            tn0, tn1, tn2 = tn1, tn2, tn0+tn1+tn2
        return tn2

    def tribonacci(self, n: int) -> int:
        if n in (0,1): return n 
        tn0, tn1, tn2 = 0, 1, 1
        for i in range(n-2):
            tn0, tn1, tn2 = tn1, tn2, tn0+tn1+tn2
        return tn2

if __name__ == '__main__':
    s = Solution()
    print(s.tribonacci(4))