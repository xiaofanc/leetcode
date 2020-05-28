class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 1
        while n >= count:
            n -= count
            count += 1
        return count-1

    def arrangeCoins(self, n: int) -> int:
        return int((math.sqrt(8*n+1)-1)/2)

if __name__ == '__main__':
    s = Solution()
    print(s.arrangeCoins(5) == 2)