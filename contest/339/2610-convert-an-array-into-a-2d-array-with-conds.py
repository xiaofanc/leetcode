
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            updated = False
            for i, l in enumerate(res):
                if n not in l:
                    l.append(n)
                    updated = True
                    break
            if not updated:
                res.append([])
                res[-1].append(n)
        return res
                    
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        k = max(count.values())
        A = list(count.elements())
        return [A[i::k] for i in range(k)]


    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        total = len(nums)
        res = []
        
        while total:
            l = []
            for k, v in count.items():
                if v > 0:
                    l.append(k)
                    count[k] -= 1
                    total -= 1
            res.append(l)
        return res




        