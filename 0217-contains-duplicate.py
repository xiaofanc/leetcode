class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numsset = set(nums)
        return len(numsset) != len(nums)

    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for n in nums:
            if n in visited:
                return True
            visited.add(n)
        return False
        
if __name__ == '__main__':
	s = Solution()
	print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))