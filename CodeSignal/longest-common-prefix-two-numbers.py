"""
arr1 = [1,2,3,5444]
arr2 = [544,5,6,7,8]
find the longest common prefix for two numbers from arr1 and arr2
"""

def longest_common_prefix(arr1, arr2):
	# TLE
	res = 0
	for n1 in arr1:
		for n2 in arr2:
			l = 0
			n1, n2 = str(n1), str(n2)
			s, f = 0, 0
			while s < len(n1) and f < len(n2) and n1[s] == n2[f]:
				l += 1
				s += 1
				f += 1
			res = max(res, l)
	return res


arr1 = [1,2,3,5444]
arr2 = [544,5,6,7,8]
print(longest_common_prefix(arr1, arr2))