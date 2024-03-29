"""
https://leetcode.com/problems/race-car/discuss/123834/JavaC%2B%2BPython-DP-solution
"""
class Solution:
    dp = {0: 0}
    def racecar(self, t):
        if t in self.dp:
            return self.dp[t]
        n = t.bit_length()
        if 2**n - 1 == t:
            self.dp[t] = n
        else:
            self.dp[t] = self.racecar(2**n - 1 - t) + n + 1
            for m in range(n - 1):
                self.dp[t] = min(self.dp[t], self.racecar(t - 2**(n - 1) + 2**m) + n + m + 1)
        return self.dp[t]

if __name__ == '__main__':
    s = Solution()
    print(s.racecar(3))  # 2