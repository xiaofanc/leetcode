from typing import List
import collections
class Solution:
    def findShortestSubArray0(self, nums: List[int]) -> int:
        s = list()
        counter = collections.Counter(nums)
        for key, count in counter.items():
            s.append((count,key))
        s = sorted(s, reverse = True)
        degree = max(counter.values())
        revnums = nums[::-1]
        lennums = len(nums)
        ans = lennums
        for n in counter:
            if counter[n] == degree:
                ans = min(ans, lennums-nums.index(n)-revnums.index(n))
        return ans
    
    # left and right index
    def findShortestSubArray1(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1
            
        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)
        
        return ans
                
    
s=Solution()
print(s.findShortestSubArray0([1,2,2,2,1,1,2,1,1]))
print(s.findShortestSubArray1([1,2,2,3,1]))

   
        