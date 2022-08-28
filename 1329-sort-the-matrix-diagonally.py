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


    # sort diag one by one using counting sort
    # Time: mxn
    # Space: min(m,n) only store one diagonal
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        def helper(i, j):
            # sort the entire diagonal using counting sort - O(n)
            counts = [0] * 100  # 1 <= mat[i][j] <= 100
            for offset in range(min(m-i, n-j)):
                counts[mat[i+offset][j+offset]-1] += 1
            
            # each diagonal can have min(m,n) numbers
            sortedNum = []
            for idx in range(len(counts)):
                while counts[idx]:
                    sortedNum.append(idx+1)
                    counts[idx] -= 1
                if len(sortedNum) == min(m,n): # early stop
                    break
            
            # populate the current diagonal
            for offset in range(min(m-i, n-j)):
                mat[i+offset][j+offset] = sortedNum.pop(0) # constant since length = 100
                
        for i in range(n):
            helper(0, i)
        
        for i in range(1, m):
            helper(i, 0)
        
        return mat

if __name__ == '__main__':
    s = Solution()
    print(s.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]])) # [[1,1,1,1],[1,2,2,2],[1,2,3,3]]




    
