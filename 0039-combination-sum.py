"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
each number can be used infinity times.

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

Time: O(N^(T/M)+1)
Let N be the number of candidates, T be the target value, and M be the minimal value among the candidates.
As we illustrated before, the execution of the backtracking is unfolded as a DFS traversal in a n-ary tree. The total number of steps during the backtracking would be the number of nodes in the tree.

Here we provide a loose upper bound on the number of nodes.
First of all, the fan-out of each node would be bounded to N - the total number of candidates.
The maximal depth of the tree, would be T/M, where we keep on adding the smallest element to the combination.
As we know, the maximal number of nodes in N-ary tree of T/M height is N^(T/M)+1.

Space: O(T/M)
We implement the algorithm in recursion, which consumes some additional memory in the function call stack.
The number of recursive calls can pile up to T/M, where we keep on adding the smallest element to the combination. As a result, the space overhead of the recursion is O(T/M).
In addition, we keep a combination of numbers during the execution, which requires at most T/M as well.
"""


class Solution:
    # time complexity: O(N^(T/M)+1)
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

     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        
        def dfs(start, remain, comb):
            if remain < 0:
                return
            if remain == 0:
                res.append(comb)
                return
            for i in range(start, n):
                dfs(i, remain-candidates[i], comb + [candidates[i]])
                
        dfs(0, target, [])
        return res       

    # Time: O(2^(T/M))
    def combinationSum3(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        
        def backtrack(index, comb, total):
            if total > target or index >= n:
                return
            if total == target:
                res.append(comb[:]) # deep copy
                return
            
            # option 1: add current value
            comb.append(candidates[index])
            backtrack(index, comb, total+candidates[index])
            comb.pop()
            # option 2: do not add current value
            backtrack(index+1, comb, total)
            
        backtrack(0, [], 0)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2,3,6,7], 7)) # [[2,2,3],[7]]



    