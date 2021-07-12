class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target

    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for i, j in zip(nums, index):
            res.insert(j, i)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.createTargetArray([0,1,2,3,4], [0,1,2,2,1]))