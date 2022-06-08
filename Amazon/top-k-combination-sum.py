"""
https://leetcode.com/discuss/interview-question/1464982/Online-Assessment-Programming-Question/1092320

Given an array of numbers(positive and negative) return the top k most combination sum(sorted).
Sample case
[5,3,-2], k=3
possible combinations sums: 5, 3, -2, 8, 6, 1, ..
answer -> [8,6,5]

90. subset-ii
347. top-k-frequent-elements
"""
class Solution:
	# TLE
	# Time complexity: 2^n*log(k)+k*log(k) Space Complexity: O(k) + O(n)->(for recursion)
    def topKcombinationSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        heap = []
        
        def backtrack(start, comb, combSum):
            heapq.heappush(heap, combSum)
            if len(heapq) > k:
            	heapq.heappop(heap)
            for i in range(start, n):
                if i > start and nums[i] == nums[i-1]: # remove duplicates - need??
                    continue
                comb.append(nums[i])
                backtrack(i+1, comb, combSum+nums[i])
                comb.pop()

        backtrack(0, [], 0)
        return sorted(heap, reverse=True)

if __name__ == "__main__":
    s = Solution()
    print(s.topKcombinationSum([5, 3, -2], 3))



