# Given an array of integers and an integer k, you need to find the total number
# of continuous subarrays whose sum equals to k.

from typing import List
from itertools import accumulate
from collections import defaultdict

class Solution:
    # Time - O(n^2); Space - O(n)
    def subarraySum(self, nums: List[int], k: int) -> int: 
        count = 0
        # accum = [0]+list(accumulate(nums))
        acc_sum = [0]*(len(nums)+1)
        acc_sum[0] = 0 # accumelative sum up to 0
        for i in range(1, len(nums)+1):
            # cumulative sum of array up to the (i-1)th element
            # to determine the sum of elements for the subarray nums[i:j], we can directly use sum[j+1] - sum[i].
            acc_sum[i] = acc_sum[i-1] + nums[i-1]
            # print(acc_sum)
        for start in range(len(nums)):
            for end in range(start+1, len(nums)+1):
                if acc_sum[end] - acc_sum[start] == k:
                    count += 1
        return count
            

    # we can directly find the sum on the go while considering different end points
    # Time - O(n^2); Space - O(1)
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for start in range(len(nums)):
            accsum = 0
            for end in range(start, len(nums)):
                accsum = accsum + nums[end]
                if accsum == k:
                    count += 1
        return count


    # method similar to 2sum, 3sum, storing running sum in the map
    # if the cumulative sum up to two indices i, j is at a difference of k, i.e. if sum[j] - sum[i] = k, the sum of elements lying between i and j is k.
    # using a hashmap, the count of (sum-k) in map is the count of subarrays that equals to k
    # Time - O(n); Space - O(n)
    # 有多少sum of subarray = sum-k 就有多少sum of subarray = k
    def subarraySum(self, nums: List[int], k: int):
        count, _sum = 0, 0
        mapp = {}
        mapp[0] = 1
        for i in range(len(nums)):
            _sum += nums[i]
            if _sum-k in mapp:
                count += mapp[_sum-k]
            if _sum in mapp:
                mapp[_sum] += 1
            else:
                mapp[_sum] = 1
        return count


    def subarraySum(self, nums: List[int], k: int):
        count, _sum = 0, 0
        mapp = defaultdict(lambda:0) # initiate as 0 if not exists
        mapp[0] = 1
        for i in range(len(nums)):
            _sum += nums[i]
            count += mapp[_sum-k]
            mapp[_sum] += 1
        return count

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        res = 0
        sign = 1 # 1 mean positive
        for ch in s:
            print("ch: %s, sign: %s, operand: %s, res: %s, stack: %s" % (ch, sign, operand, res, stack))
            if ch.isdigit():
                operand = operand*10 + int(ch) # more than one digit
            elif ch == "+":
                res += sign*operand
                sign = 1
                operand = 0  # reset operand
            elif ch == "-":
                res += sign*operand # previous sign
                sign = -1
                operand = 0
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif ch == ')':
                res += sign*operand
                res *= stack.pop()
                res += stack.pop()
                operand = 0
        return res + sign*operand
                
                
                
if __name__ == '__main__':
    s = Solution()
    print(s.subarraySum([1,-1,1,-1,1,-1,1,-1], 0))    
    assert(s.subarraySum([1,-1,1,-1,1,-1,1,-1], 0) == 16)     
                
        