from typing import List
import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #s = list()
        count = collections.Counter(nums)
        #for keys, counts in count.items():
        #    s.append((counts,keys))
        #    print(s)
        #s = sorted(s, reverse = True)
        #print(s)
        #return s[0][1]
        
        return max(count.keys(), key=count.get)
            
    
            
s = Solution()
print(s.majorityElement([1,2,3,3,5,3,6]))