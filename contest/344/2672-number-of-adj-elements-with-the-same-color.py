
class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        nums = [0]*n
        res = [0]
        if len(nums) == 1:
            return [0]*len(queries)
        for i, c in queries:
            oldc = nums[i]
            nums[i] = c
            if i == 0:
                pairs = 0
                if nums[i+1] == oldc and oldc != 0:
                    pairs -= 1
                if nums[i+1] == c and c != 0:
                    pairs += 1
            elif i == n-1:
                pairs = 0
                if nums[i-1] == oldc and oldc != 0:
                    pairs -= 1
                if nums[i-1] == c and c != 0:
                    pairs += 1
            else:
                pairs = 0
                if nums[i+1] == oldc and oldc != 0:
                    pairs -= 1
                if nums[i+1] == c and c != 0:
                    pairs += 1
                if nums[i-1] == oldc and oldc != 0:
                    pairs -= 1
                if nums[i-1] == c and c != 0:
                    pairs += 1
            res.append(res[-1]+pairs)
        return res[1:]
        

    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        nums = [0]*n
        res = []
        c = 0
        for i, color in queries:
            prec, nextc = nums[i-1] if i > 0 else 0, nums[i+1] if i < n-1 else 0
            if prec and nums[i] == prec:
                c -= 1
            if nextc and nums[i] == nextc:
                c -= 1
            nums[i] = color
            if prec and nums[i] == prec:
                c += 1
            if nextc and nums[i] == nextc:
                c += 1
            res.append(c)
        return res


                   