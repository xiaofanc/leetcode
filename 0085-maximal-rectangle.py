"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

[["1","0","1","0","0"],
 ["1","0","1","1","1"],
 ["1","1","1","1","1"],
 ["1","0","0","1","0"]]

final dp: calculate cumulative squares
[["1","0","1","0","0"],
 ["1","0","1","2","3"],
 ["1","2","3","4","5"],
 ["1","0","0","1","0"]]

k-loop: calculate the largest rectangle in histogram
maxarea at each point: min(width, dp[k][j])*(i-k+1)
when i = 1, j = 0-4, k = 1-0
[["2","0","2","0","0"],
 ["1","0","1","2","3"], 
when i = 2, j = 0-4, k = 2-0
[["1*3","0*3","1*3","0*3","0*3"],  i-k+1 = 3
 ["1*2","0*2","1*2","2*2","3*2"],  i-k+1 = 2
 ["1*1","2*1","3*1","4*1","5*1"],  i-k+1 = 1


"""

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # keep track of the number of consecutive ones each square in each row
        # the maximal width of a rectangle spanning from the original point to the current point is the running minimum of each maximal width we have encountered:maxwidth = min(maxwidth, widthhere)
        # curarea = maxwidth * (currentrow - originalrow + 1)
        # maxarea = max(maxarea, curarea)
        maxarea = 0
        dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0': continue
                width = dp[i][j] = dp[i][j-1] + 1 if j else 1
                # compute the maximum area rectangle with a lower right corner at [i, j]
                print(dp)
                # for each square, calculate the largest rectangle in histogram k = i -> 0
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    maxarea = max(maxarea, width*(i-k+1))
                    print(width, maxarea)
        return maxarea

if __name__ == '__main__':
    s = Solution()
    print(s.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))



