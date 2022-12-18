"""
The left node has the value 2 * val, and
The right node has the value 2 * val + 1.

this means, no matter a node is left or right child,
its parent is val / 2.

For query x and y, we try to find their common ancestor.
If x != y, we hadn't found yet.
So we let the bigger node go up:
if x > y, x = x / 2,
if x < y, y = y / 2,
and this take on step.
We continue to do this until x == y.

The cycle length is the number of steps plus 1.
"""
class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # how to find lowest common ancestor
        res = []
        for q1, q2 in queries:
            c = 1 # step
            # find lowest common ancester
            while q1 != q2:
                q1, q2 = min(q1, q2), max(q1, q2)//2
                c += 1
            res.append(c)
        return res


                