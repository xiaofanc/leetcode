"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. 

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Time: O(N×2^N)
Space: O(N)
The recursion call stack occupies at most O(N) space. 
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)

        def backtrack(start, comb):
            res.add(tuple(sorted(comb[:]))) # remove duplicates
            for i in range(start, n):
                comb.append(nums[i])
                backtrack(i+1, comb)
                comb.pop()
        backtrack(0, [])
        return res

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort() # in order to remove dup
        
        def backtrack(start, comb):
            res.append(comb[:])
            for i in range(start, n):
                # only works after sorting
                if i > start and nums[i] == nums[i-1]: # remove duplicates
                    continue
                comb.append(nums[i])
                backtrack(i+1, comb)
                comb.pop()
        backtrack(0, [])
        return res

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        
        def dfs(start, comb):
            res.append(comb)
            for i in range(start, n):
                # only works after sorting
                if i > start and nums[i] == nums[i-1]: 
                    continue
                dfs(i+1, comb+[nums[i]])
        
        dfs(0, [])
        return res

# debug
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        
        def backtrack(start, comb, x):
            res.append(comb[:])
            for i in range(start, n):
                print("  "*x, start, comb, 'i', i, 'nums', nums[i], nums[i-1], i > start)
                if i > start and nums[i] == nums[i-1]:
                    continue
                comb.append(nums[i])
                print("--"*x, "comb.append", comb)
                backtrack(i+1, comb, x+1)
                comb.pop()
                
        def backtrack(start, comb, x):
            res.append(comb[:])
            for i in range(start, n):
                print("  "*x, start, comb, 'i', i, 'nums', nums[i], nums[i-1], i > start)
                if i == start or nums[i] != nums[i-1]:
                    comb.append(nums[i])
                    print("--"*x, "comb.append", comb)
                    backtrack(i+1, comb, x+1)
                    comb.pop()
        
        backtrack(0, [], 0)
        return res
if __name__ == '__main__':
	s = Solution()
	print(s.subsetsWithDup([1,2,2]))


