"""
A substring is created by deleting zero or more elements from a list while maintaining the order. For example, the subsequence of [1,2,3] are [1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]. An inversion is a strictly decreasing subsequence of length 3. More formally, given an array, p = p[n] an inversion in the array is any time some p[i]>p[j]>p[k] and i<j<k.

Determine the number of inversions within a given array.
Example:
arr = [5,3,4,2,1]
The array inversions are:
[5,3,2],[5,3,1],[5,4,2],[5,4,1],[5,2,1],[3,2,1],[4,2,1]

arr = [4,2,2,1]
The array inversions are: [4,2,1]

https://leetcode.com/discuss/interview-question/777188/find-size-3-inversions-in-a-list
"""

class Solution:
	# Time: O(N^2), Space: O(N)
	def inversions(self, arr):
		# count how many numbers in the right of arr[i] are smaller than arr[i]
		largerThanRightCount = [0] * len(arr)
		for i in range(len(arr)):
			visited = set()
			for j in range(i+1, len(arr)):
				if arr[j] in visited:
					continue
				visited.add(arr[j])
				if arr[i] > arr[j]:
					largerThanRightCount[i] += 1

		res = 0
		visitedi = set()
		for i in range(len(arr)):
			if arr[i] in visitedi:
				continue
			visitedi.add(arr[i])
			visitedj = set()
			for j in range(i+1, len(arr)):
				if arr[j] in visitedj:
					continue
				visitedj.add(arr[j])
				if arr[i] > arr[j]:
					res += largerThanRightCount[j]
		return res

	# Time: O(N^2), Space: O(N)
	def inversions2(self, arr):
		res = 0
		n = len(arr)
		visited_curr = set()
		for i in range(1, n-1):
			if arr[i] in visited_curr:
				continue 
			visited_curr.add(arr[i])
			small = 0
			visited = set()
			for j in range(i+1, n):
				if arr[j] in visited or arr[j] > arr[i]:
					continue
				visited.add(arr[j])
				if arr[j] < arr[i]:
					small += 1

			great = 0
			visited = set()
			for j in range(i-1,-1,-1):
				if arr[j] in visited or arr[j] < arr[i]:
					continue
				visited.add(arr[j])
				if arr[j] > arr[i]:
					great += 1
			res += small * great
		return res


if __name__ == '__main__':
	s = Solution()
	print(s.inversions([5,3,4,2,1]))   # 7
	print(s.inversions([4,2,2,1]))     # 1
	print(s.inversions([4,4,2,2,1]))   # 1
	print(s.inversions([5,4,2,2,1]))   # 4
	print(s.inversions2([5,3,4,2,1]))   # 7
	print(s.inversions2([4,2,2,1]))     # 1
	print(s.inversions2([4,4,2,2,1]))   # 1
	print(s.inversions2([5,4,2,2,1]))   # 4









