from functools import reduce
from operator import mul
from itertools import accumulate

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_0 = nums.count(0)
        if count_0 > 1:
            return [0]*len(nums)
        product_all = reduce(mul, filter(lambda x: x != 0, nums))
        # product_all = reduce(mul, (n for n in nums if n!= 0))
        if count_0 == 1:
            return [0 if n != 0 else product_all for n in nums]
        else:
            return [product_all//n for n in nums]

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        ans[0] = 1
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
        rightp = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] = ans[i] * rightp
            rightp *= nums[i]
        return ans

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1] + list(accumulate(nums, mul))
        backward = list(accumulate(reversed(nums), mul))[-2::-1] + [1]
        return [f*b for f, b in zip(forward, backward)]
                  
if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))