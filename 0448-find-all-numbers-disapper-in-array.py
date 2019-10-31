from typing import List
class Solution:
    def findDisappearedNumbers0(self, nums: List[int]) -> List[int]:
        a = set(nums)
        res = []
        for i in range(1, len(nums)+1):
            if i not in a:
                res.append(i)
        return res
    
    def findDisappearedNumbers1(self, nums: List[int]) -> List[int]:           
        return set(list(range(1,len(nums)+1)))-set(nums)

if __name__ == '__main__':	
	s=s = Solution()
	print(s.findDisappearedNumbers0([4,3,2,7,8,2,3,1]))
	print(s.findDisappearedNumbers1([4,3,2,7,8,2,3,1]))