"""
return all fancy integer <= n
fancy integer: base 4 only includes 0 or 1

def convert_base(num, base):
    res = []
    while num > 0:
        res.insert(0, num % base)
        num = num // base
    return res

print(convert_base(5, 4))  # 11
print(convert_base(17, 4))  # 101
print(convert_base(21, 4))  # 111
print(convert_base(80, 4))  # 1100
"""

def solution(n):
    maxi = 0
    candidates = []
    for i in range(n//4+1):
        if 4**i < n:
            candidates.append(4**i)
            continue
        else:
            maxi = i
            break
    
    res = 0
    visited = set()
    # print("candidates", candidates)
    def backtrack(start, comb, combs):
        nonlocal res, visited
        # print("start ->", start, comb, combs)
        if combs not in visited and combs > 0 and combs <= n:
            res += 1
            visited.add(combs)
        for j in range(start, len(candidates)):
            comb.append(candidates[j])
            backtrack(j+1, comb, combs+candidates[j])
            comb.pop()
    
    backtrack(0, [], 0)
    return res

# return all possible subset sum < n
def subsetSum(n):
    maxi = 0
    candidates = []
    for i in range(n//4+1):
        if 4**i < n:
            candidates.append(4**i)
            continue
        else:
            maxi = i
            break

    sumSet = set()
    sumSet.add(0)  # subset can be empty
    for num in candidates:
        nextSet = set()
        for s in sumSet:
            nextSet.add(s)
            nextSet.add(s+num)
        sumSet = nextSet
    print("sumSet: ", sumSet)

    res = []
    for s in sumSet:
        if s > 0 and s <= n:
            res.append(s)
    print("res: ", res)
    return res

print(solution(10)) # 3 [1, 4, 5] => [4^0, 4^1, 4^1+4^0]
print(solution(20)) # 6 [1, 4, 5, 16, 17, 20] => [4^0, 4^1, 4^1+4^0, ....]
print(subsetSum(20)) # 6 [1, 4, 5, 16, 17, 20] => [4^0, 4^1, 4^1+4^0, ....]
    
        