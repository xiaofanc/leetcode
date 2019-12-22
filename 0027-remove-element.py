from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, 0
        while i < len(nums):
            if nums[i] == val:
                i += 1
            else:
                nums[j] = nums[i]
                j += 1
                i += 1
        return j

    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j

if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([3,2,2,3], 3) == 2)
    print(s.removeElement([0,1,2,2,3,0,4,2], 2) == 5)