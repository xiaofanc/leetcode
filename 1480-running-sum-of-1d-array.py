class Solution:

    # time: O(n), space: O(n)
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            output.append(s)
        return output

    # time: O(n), space: O(1)
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums

if __name__ == '__main__':
    s = Solution()
    print(s.runningSum([1,2,3,4]))
    print(s.runningSum([3,1,2,10,1]))
