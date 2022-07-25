"""
Given a sorted integer array nums and three integers a, b and c, apply a quadratic function of the form f(x) = ax2 + bx + c to each element nums[i] in the array, and return the array in a sorted order.
"""

class Solution:
	# Time: O(n + logn)
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        res = []
        for n in nums:
            res.append(a*n*n + b*n + c)
        return sorted(res)
        
    # Time: O(n)
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def quadratic(x):
            return a*x*x + b*x + c
        
        l, r = 0, len(nums)-1
        res = [0] * (len(nums))
        start = 0 if a < 0 else r
        while l <= r:
            lval, rval = quadratic(nums[l]), quadratic(nums[r])
            # if a >= 0: the largest quadratic(x) is in the left or right
            # populate from largest to smallest
            if a >= 0:
                if lval > rval:
                    res[start] = lval
                    l += 1
                else:
                    res[start] = rval
                    r -= 1
                start -= 1
            # elif a < 0: the smallest quadratic(x) is in the left or right
            # populate from smallest to largest
            else:
                if lval > rval:
                    res[start] = rval
                    r -= 1
                else:
                    res[start] = lval
                    l += 1
                start += 1
        return res
        
if __name__ == '__main__':
	s = Solution()
	print(s.sortTransformedArray([-4,-2,2,4], 1, 3, 5)) # [3,9,15,33]
	print(s.sortTransformedArray([-4,-2,2,4], -1, 3, 5)) # [-23,-5,1,7]



