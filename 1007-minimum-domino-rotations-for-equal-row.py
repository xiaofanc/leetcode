class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        candidates = []
        # either A[0] or B[0] will be the key value
        a, b = A[0], B[0]
        if all(a in pair for pair in zip(A, B)):
            candidates.append(a)
        if all(b in pair for pair in zip(A, B)):
            candidates.append(b)
        if candidates == []: return -1
        nA = max(map(lambda x: A.count(x), candidates))
        # max(A.count(c) for c in candidates)
        nB = max(map(lambda x: B.count(x), candidates))
        return len(A) - max(nA, nB)

    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        for x in set([A[0], B[0]]):
            if all(x in pair for pair in zip(A,B)):
                return min(len(A)-A.count(x), len(B)-B.count(x))
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.minDominoRotations([1,2,1,1,1,2,2,2], [2,1,2,2,2,2,2,2]))