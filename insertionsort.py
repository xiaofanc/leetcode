
class Solution:
	# time: O(n^2)
	# [-2, 3, -1, 5, 4, -3, 0]      i = 1
	# [-2, 3, -1(i), 5, 4, -3, 0]   3 > -1
	# [-2, -1, 3, 5, 4, -3, 0]     -2 < -1

	def insertionSort(self, arr):
		for i in range(1, len(arr)):
			num = arr[i]
			hole = i
			# shift large number and find the right position to insert
			while hole > 0 and arr[hole-1] > num:
				arr[hole] = arr[hole-1]
				hole -= 1
			arr[hole] = num 
			print(arr)
		return arr


if __name__ == '__main__':
	s = Solution()
	print(s.insertionSort([-2, 3, -1, 5, 4, -3, 0]))