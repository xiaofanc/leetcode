class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        count = 0
        p = 1
        exclude = set()
        s = 0
        while count < n:
            if p not in exclude:
                s += p
                count += 1
                exclude.add(target-p)
            p += 1
        return s
            
                
        