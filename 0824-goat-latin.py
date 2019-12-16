class Solution:
    def toGoatLatin(self, S: str) -> str:
        out = []
        for i, w in enumerate(S.split(" ")): # w is a string 
            if w[0] not in "aeiouAEIOU":
                w = w[1:] + w[:1]
            out.append(w + "ma" + "a" *(i+1))
        return " ".join(out)
            
    
    def toGoatLatin(self, S: str) -> str:       
        ans = []
        def convert(word):
            if word[0] not in "aeiouAEIOU":
                word = word[1:] + word[:1]
            return word + "ma"
        
        for i, word in enumerate(S.split()):
            ans.append(convert(word) + "a"*(i+1))
        return " ".join(ans)
            
if __name__ == '__main__':
    s = Solution()
    print(s.toGoatLatin("I speak Goat Latin"))
    print(s.toGoatLatin("The quick brown fox jumped over the lazy dog"))
        
                