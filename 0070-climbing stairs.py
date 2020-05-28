"""
fibonacci number:
f(n) = f(n-1) + f(n-2)

"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        prev, curr = 1, 2
        for i in range(n-2):
            prev, curr = curr, prev + curr
        return curr
        
if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(3) == 3)