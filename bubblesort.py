
class Solution:
	# time: O(n^2)
	# compare adjacent element
	# each pass will move the largest element to the end
    # 3 6 4 2
    # 3 4 2 6 (k=1)
    # 3 2 4 6 
    # 2 3 4 6 
	def bubbleSort(self, arr):
		for k in range(1, len(arr)): # in total, need len(arr)-1 times
			for i in range(len(arr)-k): # no need to sort the end
				if arr[i] > arr[i+1]:
					arr[i], arr[i+1] = arr[i+1], arr[i]
			print(arr)
		return arr

if __name__ == '__main__':
	s = Solution()
	print(s.bubbleSort([-2, 3, -1, 5, 4, -3, 0]))