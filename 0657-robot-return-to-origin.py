import collections

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        count = collections.Counter(moves)        
        return count["U"] == count["D"] and count["L"] == count["R"]
        # return (moves.count('R') == moves.count('L')) & (moves.count('U') == moves.count('D'))


    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        for move in moves:
            if   move == "U": x += 1
            elif move == "D": x -= 1
            elif move == "L": y += 1
            elif move == "R": y -= 1
        return x == y == 0

if __name__ == '__main__':
	s = Solution()
	print(s.judgeCircle("UD"))