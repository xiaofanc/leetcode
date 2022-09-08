
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        def search(l, r):
            while l <= r:
                # only one element left
                if l == r:
                    return l
                m = l + (r-l)//2
                # mid point is on a falling slope, search the left part to find the peak
                if nums[m] > nums[m+1]:
                    r = m
                else: # nums[i] != nums[i + 1] for all valid i
                    l = m+1
        return search(0, len(nums)-1)
                    
if __name__ == '__main__':
	s = Solution()
	print(s.findPeakElement([1,2,1,3,5,6,4])) #