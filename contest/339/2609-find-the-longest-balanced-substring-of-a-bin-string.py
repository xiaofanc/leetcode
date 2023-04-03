class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        zeros = []
        for i, char in enumerate(s):
            if char == "0":
                zeros.append(i)
        
        res = 0
        for i in zeros:
            # print("i, ", i)
            l, r = i, i
            zeross = 0
            oness = 0
            one = False
            while r < len(s):
                # print("r ", r)
                if s[r] == "0":
                    if one:
                        res = max(res, min(zeross, oness)*2)
                        break
                    zeross += 1
                else:
                    one = True
                    oness += 1
                r += 1
            if r == len(s):
                res = max(res, min(zeross, oness)*2)
        return res
                    
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        res, temp = 0,  "01"
        while len(temp) <= len(s):
            if temp in s:
                res = len(temp)
            temp = '0' + temp + '1'
        return res

    def findTheLongestBalancedSubstring(self, s: str) -> int:
        i = 0
        res = 0
        while i < len(s):
            zeros, ones = 0, 0
            while i < len(s) and s[i] == "0":
                zeros += 1
                i += 1
            while i < len(s) and s[i] == "1":
                ones += 1
                i += 1
            res = max(res, 2*min(zeros, ones))
        return res

        

            
        
