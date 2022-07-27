"""
ans = 0, it is the only rabit with this color

ans = 1, at least 2 rabitts with this color
ans = 1, can be same color as last one

ans = 2, at least 3 rabitts with this color, cannot be the same color as previous rabitts
ans = 2, can be same color as last one
ans = 2, can be same color as last one

ans = 2, cannot be same color as last one, must be different color
         at least another 3 rabitts with this color
"""

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d = {}
        count = 0
        for ans in answers:
            if ans == 0:
                count += 1
            else:
                # [2] => at least 3 rabbits with same color
                if ans not in d: 
                    d[ans] = 0
                    count += ans + 1
                else:
                    d[ans] += 1
                    # [2,2,2] => at least 3 with same color
                    # [2,2,2,2] => at least 6 rabbits with 2 colors
                    if ans == d[ans]: 
                        del d[ans]
        return count

if __name__ == '__main__':
	s = Solution()
	print(s.numRabbits([1,1,2])) # 5
	print(s.numRabbits([10,10,10])) # 11


