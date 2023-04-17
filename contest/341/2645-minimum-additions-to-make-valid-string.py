"""
Given a string word to which you can insert letters "a", "b" or "c" anywhere and any number of times, return the minimum number of letters that must be inserted so that word becomes valid.
A string is called valid if it can be formed by concatenating the string "abc" several times.
"""
class Solution:
	# 6 situations:
	# 'aa','ab','ac','ba','bb','bc','ca','cb','cc'
    def addMinimum(self, word: str) -> int:
        if len(word) == 0:
            return 3
        if len(word) == 1:
            return 2
        s = ""
        res = 0
        i = 0
        while i < len(word):
            if word[i] == "a":
                if i+1 < len(word):
                    if word[i+1] == "a":
                        res += 2
                        i += 1
                    elif word[i+1] == "b":
                        if i+2 < len(word) and word[i+2] == "c":
                            i += 3
                        else:
                            res += 1
                            i += 2
                    else:
                        res += 1
                        i += 2
                else:
                    res += 2
                    i += 1
            elif word[i] == "b":
                res += 1 # 'a'
                if i+1 < len(word):
                    if word[i+1] == "c":
                        i += 2
                    else:
                        res += 1
                        i += 1
                else:
                    res += 1
                    i += 1
            else:
                res += 2
                i += 1
        return res

"""      
Since "abc" is increasing,
so we can split the original word into k strict increasing subarray.

Initial the prev as a big char,
then iterate each char c in word.
If c <= prev, it means we need to start a new "abc",
then we increase k++.

Finally we find k, word is subsequence of "abc" repeated k times.
We return k * 3 - n.    

Same problem:
Find out the minimum k where word is subsequence of "abc" repeated k times.                    
"""

class Solution:
    def addMinimum(self, word: str) -> int:
        k, prev = 0, 'z'
        for c in word: 
            if c <= prev:  # 'aaa'
                k += 1
            prev = c
        return 3*k-len(word)

                
                
                    
                    
        
