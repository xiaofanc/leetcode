"""
Given a graph of friends who have different interests, determine which groups of friends have the most interests in common. Then use a little math to determine a value to return.

The graph will be represented as a series of nodes numbered consecutively from 1 to friends_nodes. Friendships have evolved based on interests which will be represented as weights in the graph. Any members who share the same interest are said to be connected by that interest. Once the node pairs with the maximum number of shared interests are determined, multiply the friends_nodes of the resulting node pairs and return the maximal product.

The function must return an integer denoting the maximal product of xi and yi such that xi and yi are a pair of friends that share the maximal number of Interest with each other.

Example:
Friends_nodes = 4
friends_edges = 5
friends_from  friends_to  friends_weight
1 				2 				1
1 				2 				2
2 				3 				1
2 				3 				3
2 				4 				3

Each pair of n = 4 friends is connected by the following Interest:
Pair (1, 2) shares 2 Interest (i.e., Interest 1 and 2)
Pair (1, 3) shares 1 Interest (i.e., Interest 1)
Pair (1, 4) shares 0 Interest
Pair (2, 3) shares 2 Interest (i.e., Interest 1 and 3)
Pair (2, 4) shares 1 Interest (i.e., Interest 3)
Pair (3, 4) shares 1 Interest (i.e., Interest 3)

The pairs connected by the maximal number of Interest are (1, 2) and (2, 3). Their respective products are 1 × 2 = 2 and 2 × 3 = 6. We then return the largest of these values as our answer, which is 6.

question: how to find the indirect connection?

"""

from collections import defaultdict
from itertools import combinations

# Time: O(V^2+E), space: O(V^2+E)
def find_max(friends_from, friends_to, friends_weight):
    # adjacency matrix
    weight2adjacent_mat = defaultdict(lambda :defaultdict(set))
    for f, t, w in zip(friends_from, friends_to, friends_weight):
        weight2adjacent_mat[w][f].add(t)
        weight2adjacent_mat[w][t].add(f)
    
    def dfs(node):
        if node in vis:
            return
        vis.add(node)
        connected_component.append(node)
        for n in adjacent_mat[node]:
            dfs(n)
    
    # connected component for each interest
    pair2cnt = defaultdict(int)
    for w, adjacent_mat in weight2adjacent_mat.items():
        vis = set()
        for node in adjacent_mat:
            connected_component = []
            dfs(node)
            for f, t in combinations(connected_component, 2):
                pair2cnt[(min(f, t), max(f, t))] += 1
                
    # count max
    max_interest_n = max(pair2cnt.values())
    return max(f * t for (f, t), cnt in pair2cnt.items() if cnt == max_interest_n)
            
friends_from = [1, 1, 2, 2, 2, 4, 4]
friends_to = [2, 2, 3, 3, 4, 5, 5]
friends_weight = [1, 2, 1, 3, 3, 1, 2]
# 20    
print(find_max(friends_from, friends_to, friends_weight))  

def MaxSHARED(friends_from, friends_to, friends_weight):   
	interestmap = defaultdict(lambda: defaultdict(set))
	# create the interest to adjacency map
	for source, dest, w in zip(friends_from, friends_to, friends_weight):
		interestmap[w][source].add(dest)
		interestmap[w][dest].add(source)

	# get the connected nodes for each interst
	paircount = defaultdict(int)
	for w, adjmap in interestmap.items():
		visited = set()
		for node in adjmap:
			cc = []
			dfs(node, adjmap, visited, cc)
			for s, t in combinations(cc,2):
				a, b = min(s,t), max(s,t)
				paircount[(a,b)] += 1

	# check the maximal interest
	max_interest = max(paircount.values())
	return max(a * b for (a,b), v in paircount.items() if v == max_interest)

def dfs(node, adjmap, visited, cc):
	if node in visited:
		return
	visited.add(node)
	cc.append(node)
	for neighbor in adjmap[node]:
		dfs(neighbor, adjmap, visited, cc)

# did not consider the indirect connection, could miss some cases!
def MaxSHARED2(friends_from, friends_to, friends_weight):     
	res = {}     
	for i in range(len(friends_from)):         
		a = min(friends_from[i], friends_to[i])         
		b = max(friends_from[i], friends_to[i])          
	if res.get((a, b)) is None:         
		res[(a, b)] = 1     
	else:         
		res[(a, b)] += 1     
	Ans = 0     
	max_Connection = 0     
	for Edge in res.keys():         
		max_Connection = max(max_Connection, res[Edge])     
	for Edge in res.keys():         
		if res[Edge] == max_Connection:             
			Ans = max(Ans, Edge[0] * Edge[1])      
	return Ans

friends_from = [1, 1, 2, 2, 2]
friends_to = [2, 2, 3, 3, 4]
friends_weight = [1, 2, 1, 3, 3]
print(MaxSHARED(friends_from, friends_to, friends_weight))

friends_from = [1, 1, 2, 2, 2, 4, 4]
friends_to = [2, 2, 3, 3, 4, 5, 5]
friends_weight = [1, 2, 1, 3, 3, 1, 2]
print(MaxSHARED(friends_from, friends_to, friends_weight))



