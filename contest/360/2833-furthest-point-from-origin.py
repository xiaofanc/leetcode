class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        count = collections.Counter(moves)
        res = abs(count['L']-count['R'])+count['_']
        return res
        