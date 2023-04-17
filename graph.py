
# prices[i] = weight for each node
# There is only one path for each [start, end], but a node could have multiple neighbors
# Calculate the total prices for the paths and occurrence of nodes
def dfs(node, par, dst):
	nonlocal totalcost, count
	if node == dst:
		return True
	for nei in adj[node]:
		if nei != par:
			if dfs(nei, node, dst):
				totalcost += price[nei]
				count[nei] += 1
				return True
	return False

totalcost = 0
count = Counter()
for a, b in trips:
	totalcost += prices[a]
	count[a] += 1
	dfs(a, -1, b)

# you can choose some non-adjacent nodes and halve the prices.
# calculate the maximum reduction for each node
# maximum reduction for path starting from node is fixed
# cache res for [node, canreduce]
@cache
def dfs(node, par, canreduce):
	res = 0
	if canreduce:
		res = prices[node]//2 * count[node]
	total = 0
	# calculate the max reduction for each neighbors
	for nei in adj[node]:
		if nei != par:
			if canreduce:
				cur = dfs(nei, node, False)
			else:
				cur = max(dfs(nei, node, False), dfs(nei, node, True))
			total += cur
	return res + total

# compare the max reduction starting from each node
red = 0
for i in range(n):
	red = max(red, dfs(i,-1,True), dfs(i,-1,False))

# min costs to go through every path
return totalcost - red





