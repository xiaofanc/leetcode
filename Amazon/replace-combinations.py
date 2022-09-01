"""
find all the combinations that replace the char using the char in the map.
"""

# Time: O(2^n), Space: O(m+n+k), k is the number that can be replaced in the s
def combinations(s, charMap):
	arr = [char for char in s]
	print("arr->", arr)
	res = []
	def backtrack(i, arr):
		if i == len(arr):
			return
		if arr[i] in charMap:
			temp = arr[i]
			arr[i] = charMap[arr[i]]
			print("i->>>>", i, arr, res)
			res.append("".join(arr[:]))
			backtrack(i+1, arr)
			arr[i] = temp
			print("i-<<<<", i, arr)

		# after backtracking, go to the next one
		print("next->")
		backtrack(i+1, arr)

	backtrack(0, arr)
	return res

charMap = {'a':'@', 's':'$'}
print(combinations("pass", charMap))