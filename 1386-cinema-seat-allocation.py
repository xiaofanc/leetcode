"""
We use three numbers to record whether the left, the middle or the right is occupied or not.
For n rows, the maximum number of families that can sit together are 2*n.
Then we iterate through the dictionary, if all three positions in the row was blocked, the total cnt should -2.
If less than 3 positions was blocked, the total cnt should -1.
"""


class Solution:
    # Time: O(M) - M is the size of the reserved seats
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        groups = collections.defaultdict(set)
        
        for i, j in reservedSeats:
            if j in [2, 3, 4, 5]:
                groups[i].add(0)
            if j in [4, 5, 6, 7]:
                groups[i].add(1)
            if j in [6, 7, 8, 9]:
                groups[i].add(2)
        
        res = n*2
        for v in groups.values():
            if len(v) == 3:
                res -= 2
            else:
                res -= 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.maxNumberOfFamilies(3, [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]))  # 4



