"""
https://leetcode.com/problems/minimum-reverse-operations/solutions/3368819/python3-bfs-sortedlist-keep-track-of-remaining-nodes/

if there is a 1 at position node, what neighboring nodes nei could it reach in one move?
Let i_left = max(0, node - K + 1), i_right = min(node + K - 1, n - 1) - (K - 1) be the starting positions of the subarray to be reversed. 
Then, after reversing subarray [i, i+K-1] (for i in [i_left, i_right]):
node goes to nei = i + (i+K-1) - node.
In the end, nei is chosen from some interval [lo, lo+2, ..., hi].

Let's do a standard BFS and keep track of which nodes haven't been reached by our BFS yet.
We split these by parity into remaining[0] and remaining[1]. When we have some interval [lo, lo+2, ..., hi] of potential neigbhors, 
we can query the intersection (of this interval with unvisited nodes) quickly as we only consider each unvisited neighbor once.

"""

from sortedcontainers import SortedList
class Solution:
    def minReverseOperations(self, n, p, banned_vals, K):
        remaining = [SortedList(), SortedList()]
        banned = set(banned_vals)
        for u in range(n):
            if u != p and u not in banned:
                # print("u, u&1 ", u, u&1)
                remaining[u & 1].add(u)
                # print("remaining, ", remaining)

        queue = [p]
        res = [-1] * n
        res[p] = 0
        for node in queue:
            # left and right are the smallest and the largest start position
            left = max(node - K + 1, 0)
            right = min(node + K - 1, n - 1) - (K - 1)

            # next possible positions (nei) for 1, currently 1 is on node
            lo = 2 * left + K - 1 - node
            hi = 2 * right + K - 1 - node
            # print("list(remaining[lo % 2].irange(0,2)) ", list(remaining[lo % 2].irange(0,2)))
            for nei in list(remaining[lo % 2].irange(lo, hi)):
                queue.append(nei)
                res[nei] = res[node] + 1
                remaining[lo % 2].remove(nei)
        
        return res


