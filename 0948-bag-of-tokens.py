class Solution:
    # failed, we can play in any order!
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        finalScore = 0
        def play(i, power, score):
            nonlocal finalScore
            print("i, power, score", i, power, score)
            if i >= len(tokens):
                finalScore = max(score, finalScore)
                return
            # if current power >= tokens[i], power -= tokens[i], score += 1
            if power >= tokens[i]:
                play(i+1, power-tokens[i], score+1)
            # if score >= 1, power += tokens[i], score -= 1
            if score >= 1:
                play(i+1, power+tokens[i], score-1)
            # do not play the ith token
            play(i+1, power, score)
        
        play(0, power, 0)
        return finalScore

    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        """
        If we play a token face up, we might as well play the one with the smallest value to lose less power. Similarly, if we play a token face down, we might as well play the one with the largest value to get the most power. We should always play tokens face up until exhaustion, then play one token face down and continue.
        """
        tokens.sort()
        deque = collections.deque(tokens)
        ans = score = 0
        while deque and (power >= deque[0] or score):
            # play a token face up until we cannot continue
            while deque and power >= deque[0]:
                power -= deque.popleft()
                score += 1
                ans = max(ans, score)
            
            # add max power once and continue
            if deque and score:
                power += deque.pop()
                score -= 1
        return ans

    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l, r = 0, len(tokens)-1
        ans = score = 0
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                ans = max(score, ans)
                l += 1
            elif power < tokens[l] and score:
                power += tokens[r]
                score -= 1
                r -= 1
            else: # cannot continue
                return ans
                
        return ans
        
if __name__ == '__main__':
    s = Solution()
    print(s.bagOfTokensScore([100,200,300,400], 200)) # 2

