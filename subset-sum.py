"""
return the top k subset sum for a list
list = [5,3,-2], k =3
res: 8,6,5
"""

def subsetSum(nums, k):
	sumSet = set()
	sumSet.add(0)  # subset can be empty
	for n in nums:
		nextSet = set()
		for s in sumSet:
			nextSet.add(s)
			nextSet.add(s+n)
		sumSet = nextSet
	return sorted(sumSet, reverse = True)[:k]

print(subsetSum([5,3,-2], 3))  # [8,6,5]

