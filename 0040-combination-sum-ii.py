class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # find all unique combinations
        counter = collections.Counter(candidates)
        # convert the counter table to a list of (num, count) tuples
        counters = [(c, counter[c]) for c in counter]
        #print(counters)
        res = []
        def backtrack(start, comb, counters):
            if sum(comb) == target:
                res.append(comb[:])
                return
            if sum(comb) > target:
                return
            # start point to avoid duplicates like: [1,6,1], [1,1,6]
            for i in range(start, len(counters)):
                num, freq = counters[i]
                if freq > 0:
                    comb.append(num)
                    counters[i] = (num, freq-1)
                    #print(comb, num)
                    backtrack(i, comb, counters)
                    comb.pop()
                    counters[i] = (num, freq)                    
        backtrack(0, [], counters)
        return res
                

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2([10,1,2,7,6,1,5], 8))