from collections import defaultdict
from typing import List

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        forward, backward = defaultdict(list), defaultdict(list)
        for a, b in trust:
            forward[a].append(b)
            backward[b].append(a)
        for person in range(1,N+1):
            if forward[person] == [] and len(backward[person]) == N-1:
                return person
        return -1

    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        count = [0] * (N+1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1
        try:
            return count.index(N-1, 1) # who is trusted - trust = n-1
        except:
            return -1
                

if __name__ == '__main__':
	s = Solution()
	print(s.findJudge(4,[[1,3],[1,4],[2,3],[2,4],[4,3]]))