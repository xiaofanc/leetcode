"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

helper("12345", 5) = helper("12345", 4) + helper("12345", 3)

memo stores the intermediate result:
helper["12345"]     memo = [-1,-1,-1,-1,-1,-1]
helper["12345", 5]  memo[5] = helper["12345", 5]
"""

class Solution: # time - O(n)
    def numDecodings(self, s: str) -> int:
        def helper(s, k, memo): # the last k digits
            # base case 1
            if k == 0: # empty string ""
                return 1
            # base case 2 # start with 0
            l = len(s) - k
            if s[l] == '0':  #numDecodings["011"] = 0
                return 0
            if memo[k] != -1:
                return memo[k]
            # recursion
            result = helper(s, k-1, memo)       # [2  26]   # [2  2  6]
            if k >= 2 and int(s[l:l+2]) <= 26:  
                result += helper(s, k-2, memo)  # [22  6]
            memo[k] = result
            return result
        
        memo = [-1]*(len(s)+1)  # a space for empty ""
        return helper(s, len(s), memo)
                
        
            
if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings("226"))  # 3



