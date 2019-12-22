class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        bold = [False]*len(S)
        for word in words:
            for i in range(len(S)):
                if S[i:i+len(word)] == word:
                    bold[i:i+len(word)] = [True]*len(word)
        ans = []
        if bold[0] == True:
            ans.append("<b>")
        for i in range(len(S)-1):
            ans.append(S[i])
            if bold[i] and not bold[i+1]:
                ans.append("</b>")
            elif not bold[i] and bold[i+1]:
                ans.append("<b>")
        ans.append(S[-1])
        if bold[-1]: 
            ans.append("</b>")
        return "".join(ans)
        
if __name__ == '__main__':
    s = Solution()
    print(s.boldWords(["ab","bc"], "aabcd"))