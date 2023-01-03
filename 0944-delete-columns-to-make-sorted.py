class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs), len(strs[0])
        cnt = 0
        for col in range(n):
            for row in range(1, m):
                if strs[row][col] < strs[row-1][col]:
                    cnt += 1
                    break
        return cnt

