"""
first question:
[[1,2,3,4],
 [0,1,2,3],
 [5,0,1,2]]
Each diagonal has same values: return True
[[1,2,3,4],
 [0,9,2,3],
 [5,0,1,2]]
return False

second question: 0973
"""
class Solution:
	# Time: O(M*N), space: O(1)
	def diagonalcheck(self, graph):
		m, n = len(graph), len(graph[0])
		for i in range(m-1):
			for j in range(n-1):
				# print(i, j)
				if graph[i][j] != graph[i+1][j+1]:
					return False
		return True

if __name__ == '__main__':
	s = Solution()
	print(s.diagonalcheck([[1,2,3,4],[0,1,2,3],[5,0,1,2]])) # True
	print(s.diagonalcheck([[1,2,3,4],[0,1,7,3],[5,0,1,2]])) # False
		
	