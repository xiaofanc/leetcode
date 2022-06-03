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
        m, n = len(matrix), len(matrix[0])
        left, right, up, down = 0, n-1, 0, m-1 
        res = []
        while left <= right and up <= down:
            if left == right:    # [[1],[2],[3]]
                for i in range(up, down+1):
                    res.append(matrix[i][left])
            elif up == down:     # [1,2,3]
                for j in range(left, right+1):
                    res.append(matrix[up][j])
            else:
                for j in range(left, right):
                    res.append(matrix[up][j])
                for i in range(up, down):
                    res.append(matrix[i][right])
                for j in range(right, left, -1):
                    res.append(matrix[down][j])
                for i in range(down, up, -1):
                    res.append(matrix[i][left])
            left += 1
            right -= 1
            up += 1
            down -= 1
        return res
                

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        VISITED = 101
        rows, columns = len(matrix), len(matrix[0])
        # Four directions that we will move: right, down, left, up.
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Initial direction: moving right.
        current_direction = 0
        # The number of times we change the direction.
        change_direction = 0
        # Current place that we are at is (row, col).
        # row is the row index; col is the column index.
        row = col = 0
        # Store the first element and mark it as visited.
        result = [matrix[0][0]]
        matrix[0][0] = VISITED

        # if break the inner loop 2 times (change direction 2 times doesn't work) then end
        while change_direction < 2:

            while True:
                # Calculate the next place that we will move to.
                next_row = row + directions[current_direction][0]
                next_col = col + directions[current_direction][1]

                # Break if the next step is out of bounds.
                if not (0 <= next_row < rows and 0 <= next_col < columns):
                    break
                # Break if the next step is on a visited cell.
                if matrix[next_row][next_col] == VISITED:
                    break

                # Reset this to 0 since we did not break and change the direction.
                change_direction = 0
                # Update our current position to the next step.
                row, col = next_row, next_col
                result.append(matrix[row][col])
                matrix[row][col] = VISITED

            # Change our direction.
            current_direction = (current_direction + 1) % 4
            # Increment change_direction because we changed our direction.
            change_direction += 1

        return result

if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))  # [1,2,3,6,9,8,7,4,5]
    print(s.spiralOrder([[1,2,3]]))  # [1,2,3]
    print(s.spiralOrder([[1],[2],[3]]))  # [1,2,3]


