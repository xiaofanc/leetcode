"""
https://www.youtube.com/watch?v=siKFOI8PNKM
read a m*n matrix in spiral order: [2,4,6,8,16,4,8,1,2,3,2,59,12,3,11]
          ->
    T 2 4  6  8
 ^    5 9  12 16  |
 |    2 11 3  4   v
    B 3 2  1  8  
      L       R
          <-
T = 0; B = m-1; L = 0; R = n-1;
dir = 0;
while (T <= B && L <= R):
    if (dir == 0): print topmost row (left to right)
        for i <- L right to R:
            print A[T][i]
        # after reading the topmost row, discard that row
        T += 1
        dir = 1
    elif (dir == 1): print the rightmost column (top to bottom)
        for i <- T down to B:
            print A[i][R]
        # after done
        R -= 1
        dir = 2
    elif (dir == 2): print the bottommost row (right to left)
        for i <- R left to L:
            print A[B][i]
        B -= 1
        dir = 3
    else: # dir = 3 print the leftmost column (bottom to top)
        for i <- B up to T:
            print A[i][L]
        L += 1
        dir = 0

# method2: layer-by-layer 

"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []: return []
        r0, rn, c0, cn = 0, len(matrix)-1, 0, len(matrix[0])-1
        res = []
        while rn >= r0 and cn >= c0:
            if rn == r0: # only have one row
                for i in range(c0, cn+1):
                    res.append(matrix[r0][i])
                    print(res)
            elif c0 == cn: # only have one column
                for i in range(r0, rn+1):
                    res.append(matrix[i][c0])
                    print(res)
            else:
                for i1 in range(c0, cn): # topmost row
                    res.append(matrix[r0][i1])
                    print(res)
                for i2 in range(r0, rn): # rightmost col
                    res.append(matrix[i2][cn])
                    print(res)
                for i3 in range(cn, c0, -1): # bottommost row
                    res.append(matrix[rn][i3])
                    print(res)
                for i4 in range(rn, r0, -1): # leftmost col
                    res.append(matrix[i4][c0])
                    print(res)
            #print(res)
            r0 += 1
            rn -= 1
            c0 += 1
            cn -= 1
            print(r0, rn, c0, cn)
        return res
                
                
if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))  # [1,2,3,6,9,8,7,4,5]