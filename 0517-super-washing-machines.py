"""

First we check the sum of dresses in all machines. if that number cannot be divided by count of machines, there is no solution.

Otherwise, we can always transfer a dress from one machine to another, one at a time until every machines reach the same number, so there must be a solution. In this way, the total actions is sum of operations on every machine.

Since we can operate several machines at the same time, the minium number of moves is the maximum number of necessary operations on every machine.

For a single machine, necessary operations is to transfer dresses from one side to another until sum of both sides and itself reaches the average number. We can calculate (required dresses) - (contained dresses) of each side as L and R:

L > 0 && R > 0: both sides lacks dresses, and we can only export one dress from current machines at a time, so result is abs(L) + abs(R)

L < 0 && R < 0: both sides contains too many dresses, and we can import dresses from both sides at the same time, so result is max(abs(L), abs(R))

L < 0 && R > 0 or L >0 && R < 0: the side with a larger absolute value will import/export its extra dresses from/to current machine or other side, so result is max(abs(L), abs(R))

For example, [1, 0, 5], average is 2
for 1, L = 0 * 2 - 0 = 0, R = 2 * 2 - 5= -1, result = 1
for 0, L = 1 * 2 - 1= 1, R = 1 * 2 - 5 = -3, result = 3
for 5, L = 2 * 2 - 1= 3, R = 0 * 2 - 0= 0, result = 3
so minium moves is 3

1st move:    1     0 <-- 5    =>    1     1     4
2nd move:    1 <-- 1 <-- 4    =>    2     1     3
3rd move:    2     1 <-- 3    =>    2     2     2

"""

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        s = [0] * (n+1)
        # cumulative sum before i - actual contained dresses
        # sum[i] does not include machine[i]
        for i in range(n):
            s[i+1] = s[i] + machines[i]
        if s[-1] % n:
            return -1
        avg = s[-1] // n
        res = 0
        for i in range(n):
            # need to move/add for the left side of machine[i]
            left = i * avg - s[i]
            # need to move/add for the right side of machine[i]
            right = (n-i-1) * avg - (s[-1] - s[i] - machines[i])
            # both sides lacks dresses, need to move from machine[i] once a time
            if left > 0 and right > 0:
                moves = abs(left) + abs(right)
            else: # both sides can move together
                moves = max(abs(left), abs(right))
            res = max(res, moves)
        return res

if __name__ == '__main__':
	s = Solution()
	print(s.findMinMoves([1, 0, 5])) # 3



