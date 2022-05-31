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

if __name__ == '__main__':
	s = Solution()
	print(s.hammingWeight())

