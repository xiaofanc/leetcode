
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
        #[1, 2, 3, 4]
        #[1, 1, 2, 6, 24]
        #why add 1? 因为第一位数1左边没有数字
        #forward returns for each point, the production of all left numbers
        forward = [1] + list(accumulate(nums, mul))
        #[4, 3, 2, 1]
        #[4, 12, 24, 24] -> [24, 12, 4, 1]
        #backward 为什么从-2开始？得到排除第一个数后的乘积。
        #为什么要加1？ 因为最后一个数4的右边没有数字
        backward = list(accumulate(reversed(nums), mul))[-2::-1] + [1]
        #[24, 12, 8, 6]
        #左边乘积*右边乘积 [1, 1, 2, 6, 24]*[24, 12, 4, 1]
        return [f*b for f, b in zip(forward, backward)]
                  
if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))