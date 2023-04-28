"""
You are given two arrays of integers a and b, and an array queries
Every queries can have one of the following forms:
	[0,i,x]: assign a[i] the value of x
	[1,x]: find the total number of pairs of indices i and j summing up to x
Perform the given queries in order and return an array containing the results of the queries of type [1,x]


a = [3,4], b = [1,2,3], queries = [[1,5], [0,0,1], [1,5]]
output: [2, 1]

a = [2,3], b = [1,2,2], queries = [[1,4], [0,0,3], [1,5]]
output: [3, 4]
2+2, 2+2, 3+1
[3,3], [1,2,2]
3+2, 3+2, 3+2, 3+2
"""
import collections
def replace_query_sum(a, b, queries):
	counta = collections.Counter(a)
	countb = collections.Counter(b)
	res = []
	for query in queries:
		# replace
		if query[0] == 0: 
			old, new = a[query[1]], query[2]
			counta[old] -= 1
			counta[new] += 1
		else:
			# find pairs
			target = query[1]
			pairs = 0
			for k, v in counta.items():
				pairs += v * countb[target-k]
			res.append(pairs)
	return res


a = [3,4]
b = [1,2,3]
queries = [[1,5], [0,0,1], [1,5]]
print(replace_query_sum(a, b, queries))

a = [2,3]
b = [1,2,2]
queries = [[1,4], [0,0,3], [1,5]]
print(replace_query_sum(a, b, queries))


