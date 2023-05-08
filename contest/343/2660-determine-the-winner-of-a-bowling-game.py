

class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        s1, s2 = 0, 0
        for i in range(len(player1)):
            s1 += player1[i]
            if (i >= 1 and player1[i-1] == 10) or (i >= 2 and player1[i-2] == 10):
                s1 += player1[i]
            s2 += player2[i]
            if (i >= 1 and player2[i-1] == 10) or (i >= 2 and player2[i-2] == 10):
                s2 += player2[i]
        if s1 > s2:
            return 1
        elif s1 < s2:
            return 2
        return 0
            
            
        