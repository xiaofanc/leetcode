"""
each number can be used once.
Input: candidates = [10,1,2,7,6,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Time: O(Nx2^N)
In the worst case, our algorithm will exhaust all possible combinations from the input array, which in total amounts to 2^N as we discussed before.
copy them into output list will take O(N).

sorting will take O(NlogN).

Space: O(N)
The recursion call stack occupies at most O(N) space. 
"""
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

    # Time: O(2^n)
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()
        
        def backtrack(start, remain, comb):
            if remain < 0:
                return
            if remain == 0:
                res.append(comb[:])
                return
            for i in range(start, n):
                # if the number of the subset is checked before, then skip
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                comb.append(candidates[i])
                backtrack(i+1, remain-candidates[i], comb)
                comb.pop()
        backtrack(0, target, [])
        return res                  

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()
        print(candidates)
        
        def dfs(start, remain, comb):
            if remain < 0:
                return
            if remain == 0:
                res.append(comb)
                return
            for i in range(start, n):
                # if the number of the subset is checked before, then skip
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                dfs(i+1, remain-candidates[i], comb+[candidates[i]])
        dfs(0, target, [])
        return res  

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2([10,1,2,7,6,6,1,5], 8))


