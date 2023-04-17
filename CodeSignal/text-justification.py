class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        def addToRes(i, j):
            # if only one word or last line, left-justified
            if i == j or j == len(words)-1:
                s = ""
                for w in range(i, j+1):
                    s += words[w]
                    if w != j:
                        s += " "
                s += " " * (maxWidth - len(s))
                res.append(s)
            else:
                # how to evenly distributed the spaces to j-i gap?
                spaces = maxWidth - sum([len(words[w]) for w in range(i, j+1)])
                each, d = spaces // (j-i), spaces % (j-i)
                s = ""
                for w in range(i, j+1):
                    s += words[w]
                    if w != j:
                        s += " " * each
                        if d > 0:
                            s += " "
                            d -= 1
                res.append(s)

        i = 0
        res = []
        while i < len(words):
            l = 0
            j = i
            while j < len(words) and l < maxWidth:
                l += len(words[j])
                l += 1    
                j += 1
            if l > maxWidth + 1:
                j -= 1
            addToRes(i, j-1) # inclusive
            i = j # move to next line
        return res
