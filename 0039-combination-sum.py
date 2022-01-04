class Solution:
    # time complexity is linear to the number of nodes of the execution tree
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        
        def backtrack(start, comb):
            if comb and sum(comb) > target:
                return
            if comb and sum(comb) == target:
                res.append(comb[:])
                return
            # Once a candidate is added into the current combination
            # we will not look back to all the previous candidates in the next explorations
            for i in range(start, n):
                comb.append(candidates[i])
                backtrack(i, comb)
                comb.pop()
        
        backtrack(0, [])
        return res

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        
        def backtrack(index, remain, comb):
            if remain == 0:
                # make a deep copy of the current combination
                # res.append(list(comb))
                res.append(comb[:])
                return
            elif remain < 0:
                return
            for i in range(index, n):
                comb.append(candidates[i])
                backtrack(i, remain-candidates[i], comb)
                comb.pop()
        
        backtrack(0, target, [])
        return res
        
if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2,3,6,7], 7)) # [[2,2,3],[7]]