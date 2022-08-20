"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Time: O(N⋅N!)
It takes N steps to generate a single permutation. Since there are in total N! possible permutations, at most it would take us N⋅N! steps to generate all permutations, simply assuming that there is no overlapping effort (which is not true).

Space: O(N!)
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # consider each unique number as the candidate
        counter = collections.Counter(nums)
        results = []
        # build up the permutations base on the current combinations and the remaining numbers
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                results.append(comb[:]) # results.append(comb) does not work - need deep copy
                return
            for num in counter:
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -= 1
                    # print(comb)
                    # continue the exploration
                    backtrack(comb, counter)
                    
                    # revert the choice for the next exploration
                    comb.pop()
                    counter[num] += 1
        
        backtrack([], counter)
        return results

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def backtrack(start):
            if start == n:
                res.append(nums[:])
            lookup = set()  # do not swap for the same element on the same level
            for i in range(start, n):
                if nums[i] not in lookup:
                    lookup.add(nums[i])
                    nums[start], nums[i] = nums[i], nums[start]
                    backtrack(start+1)
                    nums[start], nums[i] = nums[i], nums[start]
        backtrack(0)
        return res

    def permuteUnique(self, nums):
        res = []
        nums.sort()

        def dfs(nums, path):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                # when swapping, same element not necessary consecutive
                # this works since it is appending instead of swapping and same element will not be appended at the same level
                if i > 0 and nums[i] == nums[i-1]: 
                    continue
                dfs(nums[:i]+nums[i+1:], path+[nums[i]])
        
        dfs(nums, [])
        return res        

if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1,1,2])) # [[1,1,2],[1,2,1],[2,1,1]]


