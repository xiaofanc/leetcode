"""
2490.
A sentence is circular if:

The last character of a word is equal to the first character of the next word.
The last character of the last word is equal to the first character of the first word.

"""
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        for i in range(len(words)):
            if i == len(words)-1:
                if words[i][-1] != words[0][0]:
                    return False
                else:
                    return True
            else:
                if words[i][-1] != words[i+1][0]:
                    return False
        return True