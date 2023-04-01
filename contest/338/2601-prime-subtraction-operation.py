
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # if sorted(nums) == nums: return True (wrong -> [2,2])
        
        s = True
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                s = False
        if s == True:
            return s
                
        def isPrime(n):
            for i in range(2, int(sqrt(n))+1):
                if n % i == 0:
                    return False 
            return True
        
        for i, n in enumerate(nums):
            for m in range(n-1, 1, -1):
            	# reduce the number as much as possible just greater than the prev means we are greedy here
                if isPrime(m) and (i == 0 or (nums[i]-m > nums[i-1])):
                    nums[i] -= m
                    break
            if i > 0 and nums[i] <= nums[i-1]:
                return False
        return True
                
                