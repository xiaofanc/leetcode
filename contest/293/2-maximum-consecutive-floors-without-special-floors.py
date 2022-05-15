
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        res = 0
        special = set(special)
        floors = set(a for a in range(bottom, top+1))
        d = list(floors.difference(special))
        if d == []:
            return 0
        for i, n in enumerate(sorted(d)):
            if i == 0 or (i >= 1 and d[i] - d[i-1] == 1):
                continue
            else:
                res += 1
        return res + 1
            
if __name__ == '__main__':
	s = Solution()
	print(s.maxConsecutive(10,30,[19,10,15])) # 11  ?     
            
                
        
            
        
            
