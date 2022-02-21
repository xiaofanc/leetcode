"""
以king为中心向四周扩散，寻找第一个可以attack king的queen
"""

class Solution:
	# Time O(queens + 8N)
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        for x in [-1,0,1]:
            for y in [-1,0,1]:        
                for k in range(1,8):  # N
                    r, c = king[0] + x*k, king[1] + y*k
                    if [r,c] in queens:
                        ans.append([r,c])
                        break
        return ans

if __name__ == '__main__':
	s = Solution()
	print(s.queensAttacktheKing([[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], [0,0]))
	print(s.queensAttacktheKing([[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], [3,3]))
