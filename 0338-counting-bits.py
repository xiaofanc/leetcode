class Solution:
    def countBits(self, num: int) -> List[int]:
        return [bin(i).count("1") for i in range(num+1)] # '0b'

class Solution:
    # O(N)
    # explanation: https://www.youtube.com/watch?v=RyBM56RIWrM&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=12
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        # the highest power of 2 so far
        offset = 1
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i-offset]
        return dp


if __name__ == '__main__':
    s = Solution()
    print(s.countBits(5) == [0,1,1,2,1,2])