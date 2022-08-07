"""
6136.
You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:
i < j < k,
nums[j] - nums[i] == diff, and
nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets.

"""
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        res = []
        for i, n in enumerate(nums):
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[j] - n < diff:
                    j += 1
                elif nums[j] -n > diff:
                    break
                else:
                    if nums[k] - nums[j] > diff:
                        k -= 1
                    elif nums[k] - nums[j] < diff:
                        break
                    else:
                        res.append((i,j,k))
                        break
        return len(res)
