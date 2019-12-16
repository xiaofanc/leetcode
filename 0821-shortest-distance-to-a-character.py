class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        # left to right
        prev = float("-inf")
        ans = []
        for i in range(len(S)):
            if S[i] == C:
                prev = i
            ans.append(i - prev)
        
        prev = float("inf")
        for j in range(len(S)-1, -1, -1):
            if S[j] == C:
                prev = j
            ans[j] = min(ans[j], prev - j)
        return ans

    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        
        n = len(S)
        ans = [0 if c == C else n for c in S]
        #print(ans)
        for i in range(n-1): ans[i+1] = min(ans[i+1], ans[i]+1)
        #print(ans)
        for j in range(n-1)[::-1]: ans[j] = min(ans[j], ans[j+1]+1)
        #print(ans)
        return ans

    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        c = []
        for i, v in enumerate(S):
            if v == C:
                c.append(i) 
                
        res = []
        for i in range(len(S)):
            res.append(min([abs(i - j) for j in c]))
        return res

        # return [min([abs(i - j) for j in [x for x, y in enumerate(S) if y==C]]) for i in range(len(S))]

if __name__ == '__main__':
    s = Solution()
    print(s.shortestToChar("loveleetcode", "e"))
    #[3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

 
