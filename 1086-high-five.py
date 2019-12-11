from collections import defaultdict
from typing import List
import heapq
from heapq import heappush, heappop

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        ans = []
        stu_scores = defaultdict(list)
        for idx, score in items:
            stu_scores[idx].append(score)
        for idx, scores in stu_scores.items():
            scores.sort(reverse = True)
            top5 = scores[:5]
            avg = sum(top5) // len(top5)
            ans.append([idx, avg])
        return ans

    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list) # empty dict

        for idx, val in items:
            heapq.heappush(d[idx], val)  # {1: [89, 90], 2: [95]}
        if len(d[idx]) > 5:
            heapq.heappop(d[idx])

        res = [[i, sum(d[i]) // len(d[i])] for i in sorted(d)]

        return res

if __name__ == '__main__':
    s = Solution()
    print(s.highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))