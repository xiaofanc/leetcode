"""
You have n bags numbered from 0 to n - 1. You are given two 0-indexed integer arrays capacity and rocks. The ith bag can hold a maximum of capacity[i] rocks and currently contains rocks[i] rocks. You are also given an integer additionalRocks, the number of additional rocks you can place in any of the bags.

Return the maximum number of bags that could have full capacity after placing the additional rocks in some bags.
"""

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        res = 0
        for i in range(len(capacity)):
            capacity[i] -= rocks[i]
        capacity.sort()
        for i in range(len(capacity)):
            additionalRocks -= capacity[i]
            if additionalRocks >= 0 or capacity[i] == 0:
                res += 1
            else:
                break
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.maximumBags([2,3,4,5],[1,2,4,4],2)) # 3