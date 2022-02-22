class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.antidiag = 0

    def move(self, row: int, col: int, player: int) -> int:
        point = -1
        if player == 1:
            point = 1
        self.rows[row] += point
        self.cols[col] += point
        if col + row == self.n - 1:
            self.antidiag += point
        if col == row:
            self.diag += point
        if any(abs(line) == self.n for line in (self.rows[row], self.cols[col], self.antidiag, self.diag)):
            return player
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)