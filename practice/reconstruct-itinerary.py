"""
methodology:
1. adj list

"""
from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # adj list
        flight_dct = defaultdict(list)
        tickets.sort()
        for src, dest in tickets:
        	flight_dct[src].append(dest)
        res = ["JFK"]

        def backtrack(src):
        	if len(res) == len(tickets) + 1:
        		return True
        	temp = flight_dct[src]
        	for i, v in enumerate(temp):
        		res.append(v)
        		flight_dct[src].pop(i)

        		if backtrack(v): return True

        		res.pop()
        		flight_dct[src].insert(i, v)
        	return False

        backtrack("JFK")
        return res

    def findItinerary2(self, tickets: List[List[str]]) -> List[str]:
        # adj list
        flight_dct = defaultdict(list)
        tickets.sort(reverse = True)
        for src, dest in tickets:
        	flight_dct[src].append(dest)
        res = [1]

        def backtrack(src):
        	if len(res) == len(tickets) + 1:
        		return True
        	temp = flight_dct[src]
        	for i, v in enumerate(temp):
        		res.append(v)
        		flight_dct[src].pop(i)

        		if backtrack(v): return True

        		res.pop()
        		flight_dct[src].insert(i, v)
        	return False

        backtrack(1)
        return res

if __name__ == '__main__':
	s = Solution()
	# print(s.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
	# print(s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
	print(s.findItinerary2([[1, 2], [2,3], [3,4], [4,1]]))
	print(s.findItinerary2([[1,3], [3,1], [1,4], [4,1]]))



