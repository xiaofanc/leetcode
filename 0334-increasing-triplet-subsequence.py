
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

if __name__ == '__main__':
	s = Solution()
	print(s.increasingTriplet([2,1,5,0,4,6])) # true [0,4,6]
	