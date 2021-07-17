
class Solution:
	# time: O(nlogn)
	def mergeSort(self, arr):
		if len(arr) < 2:
			return arr
		mid = len(arr)//2
		left = arr[:mid]
		right = arr[mid:]
		# sort the left and right - divide
		self.mergeSort(left)
		self.mergeSort(right)

		# merge two sorted array - conquer
		i = j = k =0
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				arr[k] = left[i]
				i += 1
			else:
				arr[k] = right[j]
				j += 1
			k += 1
		while i < len(left):
			arr[k] = left[i]
			i += 1
			k += 1
		while j < len(right):
			arr[k] = right[j]
			j += 1
			k += 1

if __name__ == '__main__':
	s = Solution()
	arr = [-2, 3, -1, 5, 4, -3, 0]
	s.mergeSort(arr)
	print(arr)
