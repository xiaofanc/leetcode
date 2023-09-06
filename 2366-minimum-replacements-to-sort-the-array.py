"""
[2,10,20,19,1], expected = 47

traversal order: reverse
If we traverse forward, it may disrupt the sorted order of the previously processed elements on the left, and we'll end up needing more operations to sort the processed subarray again. However, if we traverse backward, we do not need to revisit the subarray again since we want to keep the back arr as large as possible.
if nums[i] > nums[i+1], maximize nums[i] after breaking:
- if nums[i] is divisible by nums[i+1], we break nums[i] into multiple nums[i+1]
- else, we break nums[i] into nums[i]/nums[i+1]+1 sorted elements with the smallest element = nums[i+1]-1 and the largest element = nums[i+1]
- if nums[i] = 7, nums[i+1] = 3, [2,2,3] is better than [1,3,3]
"""

class Solution:
	# wrong solution:
	# when nums[i] < nums[i+1], we can split nums[i+1]
	# when nums[i] < nums[i-1], we can split nums[i-1]
    def minimumReplacement(self, nums: List[int]) -> int:
        ops = 0
        if len(nums) <= 1:
            return 0
        for i in range(len(nums)-1):
            if (i == 0 and nums[i+1] >= nums[i]) or (nums[i-1] <= nums[i] <= nums[i+1]):
                continue
            else:
                if nums[i] < nums[i-1] or nums[i] < nums[i+1]:
                    return -1
                else:
                    # split nums[i]
                    arr = [nums[i-1], nums[i]-nums[i-1]]
                    ops += 1
                    while arr[-1] > nums[i+1]:
                        # continue to split
                        n = arr.pop()
                        arr.append(arr[-1])
                        arr.append(n-arr[-1])
                        ops += 1
                    else:
                        if arr[-1] == nums[i+1]:
                            continue
                        else:
                            return -1
        return ops
                        

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ops = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > nums[i+1]:
                if nums[i] % nums[i+1] == 0:
                    num_elements = nums[i] // nums[i+1]
                    nums[i] = nums[i+1]
                else:
                    num_elements = (nums[i] // nums[i+1]) + 1
                    nums[i] = nums[i] // num_elements
                ops += num_elements-1
        return ops

        
