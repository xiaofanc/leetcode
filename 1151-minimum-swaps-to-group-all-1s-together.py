"""
Minimum Swaps to Group All 1's Together:

window size = number of 1s
calculate maxOnes in the window
minSwap = window size - maxOnes
"""

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        # get the max number of 1's in the fixed window
        res = 0
        ones = data.count(1)
        curOnes = sum(data[:ones])
        left = 0
        maxOnes = curOnes
        for right in range(ones, len(data)):
            curOnes += data[right]
            curOnes -= data[left]
            left += 1
            maxOnes = max(maxOnes, curOnes)
        return ones - maxOnes

if __name__ == '__main__':
	s = Solution()
	print(s.minSwaps([1,0,1,0,1])) # 1
	