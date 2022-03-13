
def MaxSHARED(friends_nodes, friends_from, friends_to, friends_weight):     
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