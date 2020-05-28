from typing import List
from functools import reduce
import operator

class Solution:
    def singleNumber0(self, nums: List[int]) -> int:
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()
    
    def singleNumber1(self, nums: List[int]) -> int:   
        return 2*sum(set(nums)) - sum(nums)
    
    def singleNumber2(self, nums: List[int]) -> int:    
        a = 0
        for i in nums:
            a ^= i
        return a 
            
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x,y: x^y, nums, 0)
        # return reduce(operator.xor, nums, 0)
        
s = Solution()
print(s.singleNumber0([1,1,2,2,4]))
print(s.singleNumber1([1,1,2,2,4]))
print(s.singleNumber2([1,1,2,2,4]))