class Solution:

    # time: O(n^2), space: O(n)
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            res = 0
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]:
                    res += 1
            output.append(res)
        return output

    # time: O(n+nlogn), space: O(n)
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = {}
        for i, n in enumerate(sorted(nums)):
            if n not in d:
                d[n] = i
        return [d[n] for n in nums]

    # time: O(n+nlogn), space: O(n)
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedlist = sorted(nums)
        return [sortedlist.index(n) for n in nums]

if __name__ == '__main__':
    s = Solution()
    print(s.smallerNumbersThanCurrent([8,1,2,2,3]))