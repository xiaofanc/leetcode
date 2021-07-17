class Solution:
    # Time: O(nlogn)
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # mergesort
        # divide
        if len(nums) < 2:
            return
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        self.sortColors(left)
        self.sortColors(right)
        # merge
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

    # Time: O(n) one pass;
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        p2 = len(nums)-1
        curr = 0  # current element we are checking
        while curr <= p2:
            # for all idx < p0 : nums[idx < p0] = 0
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            # for all idx > p2 : nums[idx > p2] = 2
            elif nums[curr] == 2:
                nums[p2], nums[curr] = nums[curr], nums[p2]
                p2 -= 1
            else:
                curr += 1
                
if __name__ == '__main__':
    s = Solution()
    print(s.sortColors([2,0,2,1,1,0])) # [0,0,1,1,2,2]




