"""
Given a sorted array arr of distinct integers, write a function indexEqualsValueSearch that returns the lowest index i for which arr[i] == i.
Return -1 if there is no such index.
"""

def index_equals_value_search(arr):
	# binary search: O(logn)
	l, r = 0, len(arr)-1
	while l <= r:
		idx = (l+r) // 2
		# when arr[idx-1] < idx-1, left part does not have answer
		if arr[idx] == idx and (idx == 0 or arr[idx-1] < idx-1):
			return idx
		elif arr[idx] > idx:
			# search the left part
			r = idx - 1
		else:
			# search the right part
			l = idx + 1
	return -1


index_equals_value_search([-5,0,2,3,10,29]) # 2
index_equals_value_search([-6,-5,-4,-1,1,3,5,7]) # 7


