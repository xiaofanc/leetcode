"""
count number of 1.

Input is 32-bit int.
"""
class Solution:
	# Time: O(1)
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            # n shift right by 1
            # n = 101 -> 10
            n = n >> 1
        return res

    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            # n-1 get rid of 1 each time
            # n & (n-1) keep the left ones
            n = n & (n-1)
            res += 1
        return res

    def hammingWeight(self, n: int) -> int:
        res = 0
        mask = 1
        for i in range(32):
            # check every bit in the input
            if ((n & mask) != 0):
                res += 1
            # move 1 in the mask to the right to check next bit in the input
            mask <<= 1
        return res

if __name__ == '__main__':
	s = Solution()
	print(s.hammingWeight(11111111111111111111111111111101)) #31

