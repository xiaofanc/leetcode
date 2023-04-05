"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Time: O(N×2^N) to generate all subsets and then copy them into output list.
Space: O(N)
We are using O(N) space to maintain comb
"""
class Solution:
    # DFS
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def dfs(start, comb):
            res.append(comb)
            for i in range(start, n):
                dfs(i+1, comb+[nums[i]])
        dfs(0, [])
        return res

    # backtrack
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def backtrack(start, comb):
            res.append(comb[:])
            for i in range(start, n):
                comb.append(nums[i])
                backtrack(i+1, comb)
                comb.pop()
        backtrack(0, [])
        # [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]
        return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        for num in nums:
            res += [curr + [num] for curr in res]
        return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        n = nums.pop()
        res = self.subsets(nums)
        size = len(res)
        # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        for i in range(size):
            new = res[i] + [n]
            res.append(new)
        return res
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb[:])
                return
            for i in range(start, n):
                comb.append(nums[i])
                backtrack(i+1, comb)
                comb.pop()
        for k in range(n+1):
            # [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
            backtrack(0, [])
        return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(i, comb):
            if i >= len(nums):
                res.append(comb[:])
                return
            # include i
            comb.append(nums[i])
            backtrack(i+1, comb)
            comb.pop()

            # not include i
            backtrack(i+1, comb)
        backtrack(0, [])
        # [[1,2,3],[1,2],[1,3],[1],[2,3],[2],[3],[]]
        return res        

if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1,2,3]))


