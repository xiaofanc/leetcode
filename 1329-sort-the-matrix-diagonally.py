class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                # sort diagonally
                for offset in range(min(m-i, n-j)):
                    # move the smallest value to [i][j]
                    if mat[i][j] > mat[i+offset][j+offset]:
                        mat[i][j], mat[i+offset][j+offset] = mat[i+offset][j+offset], mat[i][j]
        return mat

    # Time: mxnxlog(min(m,n))
    # Space: mxn
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        hmap = defaultdict(list)
        for i in range(m):
            for j in range(n):
                heapq.heappush(hmap[i-j], mat[i][j])
        
        for i in range(m):
            for j in range(n):
                mat[i][j] = heapq.heappop(hmap[i-j])
        return mat

    # sort diag one by one using heap to save time
    # Time: mxnxlog(min(m,n))
    # Space: min(m,n) only store one diagonal
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        def helper(i, j):
            diag = []
            # sort the diagonal using heap
            for offset in range(min(m-i, n-j)):
                heapq.heappush(diag, mat[i+offset][j+offset])
            
            # populate the current diagonal
            for offset in range(min(m-i, n-j)):
                mat[i+offset][j+offset] = heapq.heappop(diag)
        
        # sort the first row and each diagonal starts on a col
        for i in range(n):
            helper(0, i)
        
        # sort the diagonal starts on a row
        for i in range(1, m):
            helper(i, 0)
        
        return mat



