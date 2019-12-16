from typing import List

class Solution:
    # does not work
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for v1 in nums1:
            i = nums2.index(v1)
            for j in range(i+1,len(nums2)):
                if nums2[j] > v1:
                    ans.append(nums2[j])
                    break
            if j == len(nums2)-1:
                ans.append(-1)
                   
        return ans
        
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nums2map = {}
        for n in nums2:
            while stack != [] and stack[-1] < n:
                nums2map[stack.pop()] = n
            stack.append(n)
        res = [nums2map.get(n, -1) for n in nums1]
        return res
            
        
                    
if __name__ == '__main__':
    s = Solution()
    print(s.nextGreaterElement([4,1,2],[1,3,4,2]) == [-1,3,-1])