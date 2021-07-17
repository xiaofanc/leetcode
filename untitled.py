
class Solution:
	# time: O(n^2)
	# swap min - in place
    # 3 6 4 2
    # 2 6 4 3
	def bubbleSort(self, arr):
		for i in range(len(arr)-1):
			# assuming i is the minimum
			min_idx = i
			# find the minimum in [i+1, .. , n-1]
			for j in range(i+1, len(arr)):
				if arr[j] < arr[min_idx]:
					min_idx = j 
			# swap arr[i] with arr[min_idx]
			# the ith position store the min
			arr[i], arr[min_idx] = arr[min_idx], arr[i]
			# print(arr)
		return arr

if __name__ == '__main__':
	s = Solution()
	print(s.selectionSort([-2, 3, -1, 5, 4, -3, 0]))