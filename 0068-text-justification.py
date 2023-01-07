"""
First part is to find enough number of words in each line but length of each line should be less then maxWidth(which is pretty straight forward).
Second part is to format each line.(which is difficult)
"""

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # pack as many words as possible
        # pad extra space in a line and spaces should be evenly distributed
        # if the number of spaces does not divede evenly between words, left should be assigned more spaces than the slots on the right
        # if a line only has one word, it should be left-justified
        # for the last line of text, it should be left-justified, and no extra space is inserted between words
        def addToRes(i, j, last):
            # if last line, left-justified
            if last:
                s = ""
                for w in range(i, j+1):
                    s += words[w]
                    if w != j:
                        s += " "
                s += " " * (maxWidth - len(s))
                res.append(s)
            else:
                # add words[i:j+1] to the res, fill in the spaces
                # if a line only has one word, it should be left-justified
                if i == j:
                    s = words[i] + " " * (maxWidth-len(words[i]))
                    res.append(s)
                else:
                    spaces = maxWidth - sum([len(words[w]) for w in range(i, j+1)])
                    # how to evenly distributed the spaces to j-i gap?
                    # 每个gap有 spaces // (j-i)，余下 spaces % (j-i)分给前面几个gap
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
                l += 1     # at least one empty space
                j += 1
                # print("l, j", l, words[j-1])
            # if l == maxWidth or maxWidth + 1, no need to remove
            if l == maxWidth or l == maxWidth + 1:
                # print("add ...", words[i], words[j-1])
                addToRes(i, j-1, False) # inclusive
            # not last line
            elif l > maxWidth + 1: 
                j -= 1 # remove j-1
                # print("remove add ...", words[i], words[j-1])
                addToRes(i, j-1, False) # inclusive
            # if last line
            # elif j == len(words): 
            else:
                addToRes(i, j-1, True)
            # j is the next start
            i = j
            # print("i ====> ", i)
        return res

# clean version
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
