class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        f, b = [0]*(len(nums)+1), [0]*(len(nums)+1)
        fset, bset = set(), set()
        for i in range(len(nums)):
            if nums[i] not in fset:
                fset.add(nums[i])
                f[i+1] = f[i]+1
            else:
                f[i+1] = f[i]
        
        for j in range(len(nums)-1,-1,-1):
            if nums[j] not in bset:
                bset.add(nums[j])
                b[j] = b[j+1] + 1
            else:
                b[j] = b[j+1]
        
        res = []
        for a, b in zip(f[1:], b[1:]):
            res.append(a-b)
        return res
            
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        prefix = defaultdict(int)
        suffix = Counter(nums)
        res = []
        for n in nums:
            prefix[n] += 1
            suffix[n] -= 1
            if suffix[n] == 0:
                del suffix[n]
            res.append(len(prefix)-len(suffix))
        return res         
            
                
                
        