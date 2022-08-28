"""
2389.
Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].
"""

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        res = []
        nums.sort()
        for q in queries:
            s = 0
            for i, n in enumerate(nums):
                if s+n <= q:
                    s += n
                else:
                    res.append(i)
                    break  # break the for-else loop
            else:  # if no break
                res.append(len(nums))
        return res
                    
                    
                    
            
            
                        
                