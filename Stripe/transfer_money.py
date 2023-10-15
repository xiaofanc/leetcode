"""
At Stripe we keep track of where the money is and move money between bank accounts to make sure their balances are not below some threshold. This is for operational and regulatory reasons, e.g. we should have enough funds to pay out to our users, and we are legally required to separate our users' funds from our own. This interview question is a simplified version of a real-world problem we have here. 
Let's say there are at most 500 bank accounts, some of their balances are above 100 and some are below. How do you move money between them so that they all have at least 100? Just to be clear we are not looking for the optimal solution, but a working one. 
Example input: 
  - AU: 80 
  - US: 140 
  - MX: 110 
  - SG: 120 
  - FR: 70 
Output: 
  - from: US, to: AU, amount: 20   
  - from: US, to: FR, amount: 20 
  - from: MX, to: FR, amount: 10 

followup1：反过来问，假设给你一系列transfer，问最后account balance是否满足条件。假设所给account balance无论如何也无法做到每个account>=100，问所给的transfer是不是best effort？
followup2：如何得到最优解？这里你需要问面试官如何定义最优解。面试官说转账次数越少越好。这样和leetcode465就很像了
然后=>继续followup问如果这个merge到production上，有什么需要注意的？注意一下exception handler，method/parameter rename一下，用支持thread safe的数据结构，etc..
"""

# [80,140,110,120,70]

def balance_accounts(arr):
    ins, outs = [], []
    transfers = []
    # s points to the accounts that need money
    for i in range(len(arr)):
        if arr[i][1] > 100:
            outs.append(i)
        elif arr[i][1] < 100:
            ins.append(i)
    i, j = 0, 0
    while i < len(ins) and j < len(outs):
        s, t = ins[i], outs[j]
        # transfer from t to s
        required = 100-arr[s][1]
        available = arr[t][1]-100
        # if t does not have enough money for s, move t to the next accounts
        if required > available:
            transfers.append((arr[t][0], arr[s][0], available))
            arr[s][1] += available
            j += 1
        elif required == available:
            transfers.append((arr[t][0], arr[s][0], available))
            i += 1
            j += 1
        # if t has extra money
        else:
            transfers.append((arr[t][0], arr[s][0], required))
            arr[t][1] -= required
            i += 1
    if i == len(ins):
        return transfers
    if j == len(outs):
        return []

import heapq
# optimization: minimize transactions
def min_transactions(arr):
    ins, outs = [], []
    transfers = []
    for i in range(len(arr)):
        if arr[i][1] > 100:
            heapq.heappush(outs, (-arr[i][1], i)) # max heap, order by money, index
        elif arr[i][1] < 100:
            heapq.heappush(ins, (arr[i][1], i)) # min heap
    while len(ins) > 0 and len(outs) > 0:
        moneyi, i = heapq.heappop(ins)
        x = heapq.heappop(outs)
        moneyj, j = -x[0], x[1]
        # transfer from j to i
        required = 100-moneyi
        available = moneyj-100
        # if j does not have enough money for i, push s back to ins
        if required > available:
            transfers.append((arr[j][0], arr[i][0], available))
            heapq.heappush(ins, (arr[i][1]+available, i))
        elif required == available:
            transfers.append((arr[j][0], arr[i][0], available))
        # if t has extra money, push t back to outs
        else:
            transfers.append((arr[j][0], arr[i][0], required))
            heapq.heappush(outs, (required-arr[j][1], j))
    if len(ins) == 0:
        return transfers
    if len(outs) == 0:
        return []


if __name__ == '__main__':
    # [('US', 'AU', 20), ('US', 'FR', 20), ('MX', 'FR', 10)]
    print(balance_accounts([["AU",80], ["US",140], ["MX",110], ["SG",120], ["FR",70]]))
    # [('US', 'FR', 30), ('SG', 'AU', 20)]
    print(min_transactions([["AU",80], ["US",140], ["MX",110], ["SG",120], ["FR",70]]))












