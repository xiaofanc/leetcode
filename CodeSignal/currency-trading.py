"""
rates: represents the currency price on the ith day
strategy: represents the operation perform on the ith day
	-1: buy, 0 hold, 1: sell
k: even, you may choose a range of exactly k consecutive elements, set the first half to 0 and the second half to 1
choose the range optimally to maximize the total profit.

note: assume it is always possible to perform buy and sell operations.

examples:
rates = [2,4,1,5,10,6]
strategy = [-1,1,0,1,-1,0]
k = 4
The original profit: 2*(-1) + 4*1 + 1*0 + 5*1 + 10*(-1) + 6*0 = -3

we have three variants of the new strategy:
strategy = [0,0,1,1,-1,0], profit = -4
strategy = [-1,0,0,1,1,0], profit = 13
strategy = [-1,1,0,0,1,1], profit = 18
so the maximum achievable profit is 18.

rates = [2,4,1,5,2,6,7]
strategy = [0,1,0,-1,1,-1,0]
k = 2
result = 8
"""

def trade(rates, strategy, k):
	res = 0
	cumsum = []
	new = [0 for _ in range(k//2)] + [1 for _ in range(k//2)]
	for i, j in zip(rates, strategy):
		res += i * j
		cumsum.append(res)

	# options
	for i in range(len(rates)-k+1):
		# sum before i
		p1 = cumsum[i-1]
		# replace starting from i
		p2 = 0
		for j in range(i, i+k):
			p2 += rates[j] * new[j-i]
		# sum after i+k-1
		p3 = cumsum[-1]-cumsum[i+k-1]
		res = max(res, p1+p2+p3)
	return res

def trade(rates, strategy, k):
	res = 0
	new = [0 for _ in range(k//2)] + [1 for _ in range(k//2)]
	for i, j in zip(rates, strategy):
		res += i * j
	total = res

	for i in range(len(rates)-k+1):
		temp = total
		for j in range(i, i+k):
			temp -= rates[j] * strategy[j]
			temp += rates[j] * new[j-i]
		res = max(res, temp)
	return res

# sliding window
def trade(rates, strategy, k):
	res = 0
	new = [0 for _ in range(k//2)] + [1 for _ in range(k//2)]
	for i, j in zip(rates, strategy):
		res += i * j
	temp = res

	for i in range(len(rates)):
		if i < k:
			temp -= rates[i] * strategy[i]
			temp += rates[i] * new[i]
		else:
			res = max(res, temp)
			temp += rates[i] * (1 - strategy[i])     # add new strategy[i] -> 1
			temp += rates[i-k] * strategy[i-k]       # remove the first 0 -> strategy[i]
			temp -= rates[i-k//2]                    # remove the change 1 -> 0
	res = max(res, temp)
	return res

rates = [2,4,1,5,10,6]
strategy = [-1,1,0,1,-1,0]
k = 4
print(trade(rates, strategy, k))

rates = [2,4,1,5,2,6,7]
strategy = [0,1,0,-1,1,-1,0]
k = 2
print(trade(rates, strategy, k))





