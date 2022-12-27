class Solution:
    # passed 49/57
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        dct = {}
        res = [0]*len(queries)
        for i, q in enumerate(queries):
            dct[q] = i
        
        nums.sort()
        queries.sort()
        i = 0
        s = 0
        for q in queries:
            while i < len(nums):
                if s + nums[i] <= q:
                    s += nums[i]
                    i += 1
                else:
                    break
            res[dct[q]] = i
        return res

    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        res = []
        for q in queries:
            idx = bisect.bisect_right(nums, q)
            res.append(idx)
        return res

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
                    break
            else:
                res.append(len(nums))
        return res
                    
                    
                    
            
            
                        
                

        