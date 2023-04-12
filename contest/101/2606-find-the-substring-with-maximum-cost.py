# If the character is not in the string chars, then its value is its corresponding position (1-indexed) in the alphabet.
# For example, the value of 'a' is 1, the value of 'b' is 2, and so on. The value of 'z' is 26.
# Otherwise, assuming i is the index where the character occurs in the string chars, then its value is vals[i]
# Return the maximum cost among all substrings of the string s.

class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:

        dct = {v:i for i, v in enumerate(chars)}
        res = 0
        subs = None
        for i in range(len(s)):
            if s[i] in dct:
                v = vals[dct[s[i]]]
            else:
                v = ord(s[i])-ord('a')+1
            if subs == None:
                subs = v
            else:
                # subs = max(v, subs+v)
                # max sum of substring ends with s[i]
                subs = max(subs, 0) + v
            res = max(res, subs)
        return res
            
        
        
