"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Time: O(MxNx(4^L))
for each direction, run recursive call L times

Space: O(L)
The main consumption of the memory lies in the recursion call of the backtracking function. The maximum length of the call stack would be the length of the word. Therefore, the space complexity of the algorithm is O(L).

"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        height = len(board)
        width = len(board[0])

        def backtrack(row, col, word):
            # base case:
            if len(word) == 0:
                return True
            # check the current status
            if (row < 0 or row >= height) or (col < 0 or col >= width) or board[row][col] != word[0]:
                return False
            # mark as visited
            board[row][col] = "#"
            # print(board)
            # continue
            ret = False
            for dx, dy in directions:
                ret = backtrack(row+dx, col+dy, word[1:])
                if ret: break
            # revert the change
            board[row][col] = word[0]
            # print(board)
            return ret
        
        # why for-loop outside? 
        for row in range(height):
            for col in range(width):
                if backtrack(row, col, word):
                    return True
        
if __name__ == '__main__':
    s = Solution()
    print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")) # True       

            
            