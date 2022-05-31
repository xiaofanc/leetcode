
class Solution:
	# time: O(nlogn)
	def quickSort(self, arr, l, r):
		if l >= r:
			return
		# after partition
		# numbers less than pivot are in the left of the pivot
		# numbers larger than pivot are in the right of the pivot
		# return the index of the pivot
		# [-2, -1, 0, [1], 2, 4, 3]
		p = self.partition(arr, l, r)
		# sort the left of pivot
		self.quickSort(arr, l, p-1)
		self.quickSort(arr, p+1, r)

	def partition(self, arr, l, r):
		# choose the last element as pivot
		# all the numbers that until i is less than pivot
		# all the numbers that between i and j is larger than pivot
		# [2, 1, 4, 3(i), 13, 16, 12(j), 5, 10(pivot)]
		# move j to the next 5, which is less than 10, then increment i and swap
		# [2, 1, 4, 3, 5(i), 16, 12, 13(j), 10]
		# last step: swap i+1 with pivot to make pivot in the middle
		# [2, 1, 4, 3, 5(i), 10, 12, 13(j), 16]
		# return i+1
		pivot = arr[r]
		i = l-1
		for j in range(l, r):
			# if current number is smaller than pivot
			if arr[j] < pivot:
				i += 1 # increment i
				arr[i], arr[j] = arr[j], arr[i]
		# swap i+1 with pivot to make pivot in the middle
		arr[i+1], arr[r] = arr[r], arr[i+1]
		return i+1

if __name__ == '__main__':
	s = Solution()
	arr = [-2, 3, -1, 5, 4, -3, 0]
	s.quickSort(arr, 0, 6)
	print("Sorted array is: ", arr)






