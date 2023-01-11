"""
https://leetcode.com/problems/can-i-win/solutions/159797/python-98-5-simple-readable-code-with-good-comments/

Base case?
why the stop condition is `if choices[-1] >= remainder: return True`?
if remainder is not in the choices, it does not guarantee that the current player can win right? For example, if choices = [1,3,8], left= 4?
However, when I change the condition to `if remainder in choices: return True`, it did not pass all the cases..

Why only cache choices?
left not needed since it can be calculted using desiredTotal and choices made.
"""

class Solution:
    # Time = O(n*2^k) where n = desiredTotal and k = maxChoosableInteger. Since the worst case is that you try every single subset of k on each possible remainder.
    # The value 2^k comes from the number of states in this game. Note that a state of the game is completely determined by the still available numbers in the pool, which is a subset of the initial pool [1, k] and the number of subsets is exactly 2^k.
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        choices = [i for i in range(1, maxChoosableInteger+1)]
        # no one can win
        if sum(choices) < desiredTotal:
            return False 
        # first player can win if there is odd number of choices and sum of choices == total
        if sum(choices) == desiredTotal:
            return maxChoosableInteger % 2
        
        if desiredTotal == 0:
            return True
        
        memo = {}
        def canWin(choices, left):
            # if left is in the choices ??
            if choices[-1] >= left:
                return True

            s = str(choices)
            # left not needed since it can be calculted using desiredTotal and choices made
            if s in memo:
                return memo[s]

            # select which choice to make the second player no chance to win
            for i in range(len(choices)):
                # if the second player cannot win any way
                if not canWin(choices[:i]+choices[i+1:], left-choices[i]):
                    memo[s] = True
                    return True
            
            memo[s] = False
            return False
        
        return canWin(choices, desiredTotal)

