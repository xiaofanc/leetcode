class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        char1 = collections.Counter(word1)
        char2 = collections.Counter(word2)
        if char1 == char2:
            return True
        elif abs(len(char1)-len(char2)) > 2:
            return False
        else:
            c1 = char1.copy()
            c2 = char2.copy()
            for k1, v1 in char1.items():
                for k2, v2 in char2.items():
                    if k1 == k2:
                        continue
                    else:
                        # swap
                        c1[k1] -= 1
                        if c1[k1] == 0:
                            del c1[k1]
                        c2[k2] -= 1
                        if c2[k2] == 0:
                            del c2[k2]
                        c1[k2] += 1
                        c2[k1] += 1
                        if len(c1) == len(c2):
                            return True
                        else:
                            c1 = char1.copy()
                            c2 = char2.copy()
        return False
                            
    def isItPossible(self, word1: str, word2: str) -> bool:
        char1 = collections.Counter(word1)
        char2 = collections.Counter(word2)
        c1 = len(char1)
        c2 = len(char2)

        if c1 == c2 and len(word1) == len(word2):
            return True
        elif abs(c1-c2) > 2:
            return False
        else:
            for k1, v1 in char1.items(): # <= 26
                for k2, v2 in char2.items(): # <= 26
                    if k1 == k2:
                        continue
                    else:
                        c1c, c2c = c1, c2
                        if char1[k1] == 1: c1c -= 1
                        if char1[k2] == 0: c1c += 1
                        if char2[k2] == 1: c2c -= 1
                        if char2[k1] == 0: c2c += 1
                        if c1c == c2c:
                            return True
        return False                    
                
                
        