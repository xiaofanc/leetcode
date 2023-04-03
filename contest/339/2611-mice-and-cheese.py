"""
sorting does not work:
add the largest k from the reward1 does not guarantee the sum is maximum !!

[1,4,4,6,4]
[6,5,3,6,1]
1
The first mice should eat 4 and the secone mice eats [6,5,3,6], total = 24

Assume take all from the second array.
Check the difference sequence:
A[0] - B[0], A[1] - B[1], ...

Take k largest from the sequence and sum up.
Return the res = sum(B) + sum(k largest A[i]-B[i])
"""
class Solution:
	# TLE: 503 / 564 testcases passed
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        def subset(reward1, reward2):
            res = 0
            n = len(reward1)

            def dfs(start, comb, selected):
                nonlocal res
                if len(comb) == k:
                    s = sum(comb)
                    for j in range(n):
                        if j not in selected:
                            s += reward2[j]
                    res = max(res, s)
                    return
                for i in range(start, n):
                    selected.add(i)
                    dfs(i+1, comb+[reward1[i]], selected)
                    selected.remove(i)
            dfs(0, [], set())
            return res
        return subset(reward1, reward2)


    def miceAndCheese(self, r1: List[int], r2: List[int], k: int) -> int:
    	# select k from r1
        return sum(r2) + sum(nlargest(k, (a-b for a, b in zip(r1, r2))))

        # select k from r1
        # diff = [(a-b) for a, b in zip(r1, r2)]
        # diff.sort(reverse = True)
        # return sum(r2) + sum(diff[:k])

        # select n-k from r2
        # diff = [(b-a) for a, b in zip(r1, r2)]
        # diff.sort(reverse = True)
        # n = len(r1)
        # return sum(r1) + sum(diff[:n-k])




