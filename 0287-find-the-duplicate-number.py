class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def store(nums, cur):
            if cur == nums[cur]:
                return cur
            nxt = nums[cur]
            nums[cur] = cur
            return store(nums, nxt)

        return store(nums, 0)

    def findDuplicate(self, nums: List[int]) -> int:
        while nums[0] != nums[nums[0]]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
        return nums[0]

    # binary search
    def findDuplicate(self, nums: List[int]) -> int:
        # for each number, the count of numbers <= the number, is equal to itself
        # if the count > itself, then it could be possible ans
        # find the smallest number such that the count of numbers <= it is greater than the number itself
        left, right = 1, len(nums)
        while left <= right:
            cur = left+(right-left)//2
            count = sum(num <= cur for num in nums)
            if count <= cur:
                left = cur + 1
            else:
                ans = cur
                right = cur - 1
        return ans

    # linked list - find the entrance of the cycle
    def findDuplicate(self, nums: List[int]) -> int:
        # linked list cycle: 2(F + a) = F + nC + a
        slow, fast = nums[0], nums[0]
        # find where they meet
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # find where the cycle begins: F = nC-a
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


