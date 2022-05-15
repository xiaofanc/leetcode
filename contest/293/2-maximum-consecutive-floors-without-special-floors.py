"""
Return the maximum number of consecutive floors without a special floor.
"""
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        res = 0
        special = sorted(special)
        i = 0
        l = bottom
        while i < len(special):
            res = max(res, special[i]-l)
            l = special[i] + 1
            i += 1
        return max(res, top-l+1)
        
if __name__ == '__main__':
	s = Solution()
	print(s.maxConsecutive(10,30,[19,10,15])) # 11  30-20+1 = 11     
            
                
        
            
        
            
