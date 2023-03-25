class Solution:
    # wrong! This is to calculate how many subarray with sum = 0
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ss = {0:1}
        s = 0
        cnt = 0
        for i in range(len(nums)):
            s += nums[i]
            if s in ss:
                cnt += ss[s]
            ss[s] = ss.get(s, 0) + 1
        return cnt

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        nums = [0] + nums
        cnt = 0
        d = 0
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            if nums[i] == nums[i-1]:
                d += 1
                cnt += d
            else:
                d = 0
        return cnt

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                end = i
                while end < len(nums) and nums[end] == 0:
                    end += 1
                # count subarrays for nums[i:end]
                cnt += (end-i+1)*(end-i)//2
                i = end + 1
            else:
                i += 1
        return cnt

    # same as before
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt = 0  # count continuous zeros
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt += 1
            else:
                res += cnt * (cnt+1) // 2
                cnt = 0
        res += cnt * (cnt+1) // 2
        return res

    # If num != 0, there will not be any 0-filled subarray ends with it. 
    # Otherwise, it depends on how many 0-filled subarrays end with the previous number.
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt = 0
        subarray = 0 # count 0-filled subarrays end with current num
        for i in range(len(nums)):
            if nums[i] == 0:
                subarray += 1
                cnt += subarray
            else:
                subarray = 0
        return cnt



