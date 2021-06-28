class Solution:
    # time: O(n^2), space: O(1)
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                #print(i,j)
                #print("nums: ",nums[i], nums[j])
                if nums[i] == nums[j]:
                    pairs += 1
        return pairs

    # time: O(n), space: O(n)
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a, pairs = collections.Counter(nums), 0

        for k, v in a.items():
            pairs += v*(v-1)//2
        return pairs

    # time: O(n^2), space: O(1)
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        i, j = 0, 1
        while i < j:
            if j == len(nums):
                i += 1
                j = i+1
            if i == len(nums)-1:
                break
            if nums[i] == nums[j]:
                pairs += 1
                j += 1
            else:
                j += 1
        return pairs

if __name__ == '__main__':
    s = Solution()
    print(s.numIdenticalPairs([1,2,3,1,1,3]))  #4