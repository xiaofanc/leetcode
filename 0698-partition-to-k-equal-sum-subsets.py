"""
target = sum(nums) / k

We are traversing the entire array for each subset (once we are done with one subset, for the next subset we are starting again with index 0). So for each subset, we are choosing the suitable elements from the array (basically iterate over nums and for each element either use it or skip it, which is O(2^n) operation

Time: O(kx2^n)
Space: O(n)
We have used an extra array of size N to mark the already used elements.
And the recursive tree makes at most N calls at one time, so the recursive stack also takes O(N) space.

"""

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        nums.sort(reverse = True)
        target = sum(nums) / k
        used = [False] * len(nums)

        def backtrack(i, cursum, k):
            if k == 0:
                return True
            if cursum == target:
                # start to tranverse from beginning
                return backtrack(0, 0, k-1)
            
            for j in range(i, len(nums)):
                # if there is an element that was skipped earlier, then that element will be skipped again because now the subset-sum has increased; if it did not fit in the subset earlier, it would not fit now.
                if used[j] or cursum + nums[j] > target or (j > 0 and nums[j] == nums[j-1] and not used[j-1]):
                    continue
                used[j] = True
                if backtrack(j+1, cursum+nums[j], k):
                    return True
                used[j] = False
            return False
                
        return backtrack(0, 0, k)

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        nums.sort(reverse = True)
        target = sum(nums) / k
        used = [False] * len(nums)

        def backtrack(i, cursum, count):
            if count == k-1:
                return True
            if cursum == target:
                # start to tranverse from beginning
                return backtrack(0, 0, count+1)
            if cursum > target:
                return False
            
            for j in range(i, len(nums)):
            	# if nums[j] is used or (nums[j] == nums[j-1] and nums[j-1] was skipped), then skip nums[j]
                if used[j] or (j>0 and nums[j] == nums[j-1] and not used[j-1]):
                    continue
                used[j] = True
                # if using current jth element in this subset leads to make all valid subsets.
                if backtrack(j+1, cursum+nums[j], count): return True
                used[j] = False
                    
            return False
                
        return backtrack(0, 0, 0)

if __name__ == '__main__':
	s = Solution()
	print(s.canPartitionKSubsets([2,9,4,7,3,2,10,5,3,6,6,2,7,5,2,4], 7)) # False



            
                