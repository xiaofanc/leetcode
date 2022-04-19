"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
	- Only numbers 1 through 9 are used.
	- Each number is used at most once.

Time: O(9!*K/(9-K)!)
The number of exploration we need to make in the worst case would be P(9, K) = 9!/(9-K)!
Each exploration takes a constant time to process, except the last step where it takes O(K) time to make a copy of combination.

Space: O(K)
During the backtracking, we used a list to keep the current combination, which holds up to K elements.
Since we employed recursion in the backtracking, we would need some additional space for the function call stack, which could pile up to K consecutive invocations.
To sum up, the overall space is O(K)

"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [i for i in range(1,10)]
        res = []
        
        def backtrack(idx, k, remain, comb):
            if remain < 0:
                return 
            if remain == 0 and k == 0:
                res.append(comb[:])
                return
            for i in range(idx, 9):
                comb.append(candidates[i])
                backtrack(i+1, k-1, remain-candidates[i], comb)
                comb.pop()
        backtrack(0, k, n, [])
        return res

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [i for i in range(1,10)]
        res = []
        
        def dfs(idx, k, remain, comb):
            if remain < 0:
                return True
            if remain == 0 and k == 0:
                res.append(comb)
                return True
            for i in range(idx, 9):
                stop = dfs(i+1, k-1, remain-candidates[i], comb+[candidates[i]])
                if stop: break
        dfs(0, k, n, [])
        return res

if __name__ == '__main__':
	s = Solution()
	print(s.combinationSum3(3, 9)) # [[1,2,6],[1,3,5],[2,3,4]]

