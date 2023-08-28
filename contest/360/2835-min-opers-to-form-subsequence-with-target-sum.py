"""
How to prove that it works?
"""
class Solution:
	# Time: O(nlogn)
    def minOperations(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if total < target:
            return -1
        nums.sort()
        ops = 0
        while target > 0:
            n = nums.pop()
            # we do not need n 
            if total-n >= target:
                total -= n
                continue
            # we use n if n <= target
            elif n <= target:
                total -= n
                target -= n
            else: # split n
                nums.append(n//2)
                nums.append(n//2)
                ops += 1
        return ops
                
                
        