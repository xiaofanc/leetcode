"""
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Time: O(|E|^d)
where ∣E∣ is the number of total flights and d is the maximum number of flights from an airport.

Space: O(∣V∣+∣E∣)
dct takes the space ∣V∣+∣E∣
recursion maximum depth = the number of flights in the input = |E|

"""

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # create the Adj list
        dct = defaultdict(list)
        # get smaller lexical order first
        # tickets.sort(key = lambda x: (x[0], x[1]))
        tickets.sort()
        for src, dest in tickets:
            dct[src].append(dest)
        # print("dct->", dct)
        res = ["JFK"]
        
        def backtrack(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in dct:
                return False
            temp = dct[src]
            for i, v in enumerate(temp):
                # update the actual list for backtracking
                dct[src].pop(i)
                res.append(v)
                # if one path is found
                if backtrack(v): return True
                
                dct[src].insert(i, v)
                res.pop()
                
            return False                
        
        backtrack("JFK")
        return res
                
            
if __name__ == '__main__':
	s = Solution()
	print(s.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])) # ["JFK","NRT","JFK","KUL"]


