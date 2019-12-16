class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        ans = []
        zipped = zip(sorted_nums, nums)
        for i in range(len(zipped)):
            if zipped[i][0] != zipped[i][1]:
                ans.append(i)
        if ans == []:
            return 0
        return max(ans) - min(ans) + 1
        #ans = [[i if zipped[i][0] != zipped[i][1] for i in range(len(zipped))]]
        #print(ans)

    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [i for (i, (a, b)) in enumerate(zip(nums, sorted(nums))) if a != b]
        return 0 if res == [] else res[-1] - res[0] + 1

    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        is_same = [a == b for a, b in zip(nums, sorted(nums))]
        return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)

if __name__ == '__main__':
    s = Solution()
    print(s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))

    