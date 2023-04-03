"""
dp[remain][row][col] = # ways to cut the rectangular part pizza[row..rows-1][col..cols-1] with remain cuts

base case:
remain = 0, if pizza[row..rows-1][col..cols-1] contains at least one apple, dp[remain][row][col] = 1, else dp[remain][row][col] = 0

transition function for remain > 0:
dp[remain][row][col] = the sum of dp[remain-1][next_row][col] and dp[remain-1][row][next_col] for all valid values of next_row and next_col.

how to quickly verify if a rectangle has an apple for valid next_row and next_col?
apples[row][col] denote the number of apples on pizza[row..rows-1][col..cols-1] (so apples[0][0] will be the number of apples on the original pizza).
The matrix apples is the cumulative region sum matrix. One can calculate this matrix using the reccurrence relation apples[row][col] = (pizza[row][col] == 'A') + apples[row + 1][col] + apples[row][col + 1] - apples[row + 1][col + 1]
Having the matrix apples one can find the number of apples on pizza[row..next_row-1][col..cols-1] as apples[row][col] - apples[next_row][col] and on pizza[row..rows-1][col..next_col-1] as apples[row][col] - apples[row][next_col]
"""

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        rows, cols = len(pizza), len(pizza[0])
        apples = [[0 for j in range(cols+1)] for i in range(rows+1)]
        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                apples[i][j] = (pizza[i][j] == 'A') + apples[i+1][j] + apples[i][j+1] - apples[i+1][j+1]
        
        dp = [[[0 for col in range(cols)] for row in range(rows)] for _ in range(k)]
        # base case: k = 0
        for row in range(rows):
            for col in range(cols):
                dp[0][row][col] = int(apples[row][col] > 0)

        mod = 10 ** 9 + 7
        for remain in range(1, k):
            for row in range(rows-1,-1,-1):
                for col in range(cols-1,-1,-1):
                    res = 0
                    for nextr in range(row+1, rows):
                        if apples[row][col] - apples[nextr][col] > 0:
                            res += dp[remain-1][nextr][col]
                    for nextc in range(col+1, cols):
                        if apples[row][col] - apples[row][nextc] > 0:
                            res += dp[remain-1][row][nextc]
                    dp[remain][row][col] = res % mod
        return dp[k-1][0][0]


    def ways(self, pizza: List[str], k: int) -> int:
        rows, cols = len(pizza), len(pizza[0])
        apples = [[0 for j in range(cols+1)] for i in range(rows+1)]
        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                apples[i][j] = (pizza[i][j] == 'A') + apples[i+1][j] + apples[i][j+1] - apples[i+1][j+1]
        
        prev = [[0 for col in range(cols)] for row in range(rows)]
        # base case: k = 0
        for row in range(rows):
            for col in range(cols):
                prev[row][col] = int(apples[row][col] > 0)
        # k > 0
        mod = 10 ** 9 + 7
        for remain in range(1, k):
            dp = [[0 for col in range(cols)] for row in range(rows)]
            for row in range(rows-1,-1,-1):
                for col in range(cols-1,-1,-1):
                    # options
                    for nextr in range(row+1, rows):
                        if apples[row][col] - apples[nextr][col] > 0:
                            dp[row][col] += prev[nextr][col]
                    for nextc in range(col+1, cols):
                        if apples[row][col] - apples[row][nextc] > 0:
                            dp[row][col] += prev[row][nextc]
                    dp[row][col] %= mod
            prev = dp
        return prev[0][0]



        
