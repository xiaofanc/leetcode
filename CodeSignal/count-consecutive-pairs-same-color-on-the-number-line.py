"""
There is a number line of length l, color the coordinate with queries.
Count the consecutive pairs of coordinate with same color.

length = 7, queries = [(1,2),(0,2),(3,5),(3,2),(2,2),(6,1),(1,3)]
res = [0,1,1,1,3,3,1]
"""

# 18/20 passed
def count_pairs(length, queries):
	res = []
	dct = {}   # color of i
	pairs = {} # pairs with i for the current color
	prev = 0
	for i, c in queries:
		cur = prev
		# overwrite the color and remove the pairs
		if i in dct and dct[i] != c:
			if i-1 in dct and dct[i-1] == dct[i]:
				pairs[i-1] -= 1
				pairs[i] -= 1
				cur -= 1
			if i+1 in dct and dct[i+1] == dct[i]:
				pairs[i+1] -= 1
				pairs[i] -= 1
				cur -= 1
		else:
			pairs[i] = 0
		# count new pairs for i
		if i-1 in dct and dct[i-1] == c:
			pairs[i] += 1
			pairs[i-1] += 1
			cur += 1
		if i+1 in dct and dct[i+1] == c:
			pairs[i] += 1
			pairs[i+1] += 1
			cur += 1
		dct[i] = c
		prev = cur # new number of pairs
		res.append(cur)
	return res

length = 7
queries = [(1,2),(0,2),(3,5),(3,2),(2,2),(6,1),(1,3)]
print(count_pairs(length, queries)) # res = [0,1,1,1,3,3,1]



