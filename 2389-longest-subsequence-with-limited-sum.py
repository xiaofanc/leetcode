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
