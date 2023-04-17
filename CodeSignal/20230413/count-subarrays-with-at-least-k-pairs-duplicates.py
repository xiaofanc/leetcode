"""
You are given an array of integers and a positive integer k.
Count the number of contiguous subarrays within numbers that contains at least k pairs of elements with duplicate values.

More formally, count the number of contiguous subarrays for which ther are 2*k elements (with pairwise distinct indices)
with each pair having the same value.

numbers = [0,1,0,1,0]
k = 2
solution = 3: [0,1,0,1], [0,1,0,1,0], [1,0,1,0]

numbers = [1,3,3,1]
k = 1
solution = 4: [1,3,3], [1,3,3,1], [3,3], [3,3,1]

numbers = [2,2,2,2,2,2]
k = 3
solution = 1: [2,2,2,2,2,2]

one integer can only be selected for one pair
"""

def count_subarrays(numbers, k):
	res = 0
	for i in range(len(numbers)):
		count = {}
		pairs = 0
		j = i
		while j < len(numbers):
			if numbers[j] not in count:
				count[numbers[j]] = 1
			else:
				pairs -= count[numbers[j]] // 2
				count[numbers[j]] += 1
				pairs += count[numbers[j]] // 2
			if pairs == k:
				res += len(numbers)-j
				break # j
			j += 1
	return res

numbers = [0,1,0,1,0]
k = 2
# solution = 3: [0,1,0,1], [0,1,0,1,0], [1,0,1,0]
print(count_subarrays(numbers, k))

numbers = [1,3,3,1]
k = 1
# solution = 4: [1,3,3], [1,3,3,1], [3,3], [3,3,1]
print(count_subarrays(numbers, k))

numbers = [2,2,2,2,2,2]
k = 3
# solution = 1: [2,2,2,2,2,2]
print(count_subarrays(numbers, k))



