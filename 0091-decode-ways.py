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

A cell with index i of the dp array is used to store the number of decode ways for substring of s from index 0 to index i-1.
"""
def memo(f):
    m = {}
    def wrapper(*args): # new function
        if args not in m:            
            m[args] = f(*args)
            # f(self, '12') = numDecoding(self, '12')
            # m {[self, '12']: 2}
        return m[args]
    return wrapper

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
                
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if int(s[0]) == 0 or n == 0:
            return 0
        if n == 1:
            return 1
        prev = int(s[0])
        dp = [1] * (n+1)
        for i in range(2, n+1):
            cur = int(s[i-1])
            if (prev == 0 or prev > 2) and cur == 0:
                return 0
            if (prev < 2 and prev > 0) or prev == 2 and cur < 7:
                if cur:
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-2]
            else:
                dp[i] = dp[i-1]
            prev = cur
        return dp[n]

    def numDecodings(self, s: str) -> int:
        """
        dp[i] = Number of ways of decoding substring s[:i]
        """
        n = len(s)
        # if the string is empty 
        if n == 0:
            return 0
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1
        for i in range(2, n+1):
            # check if single digit decoding is possible
            if s[i-1] != "0":
                dp[i] = dp[i-1]
            # check if two digits decoding is possible
            if int(s[i-2:i]) >= 10 and int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
                
        return dp[n]

    @memo
    def numDecodings(self, s: str) -> int:
        """
        dp[i] = Number of ways of decoding substring s[:i]
        """
        n = len(s)
        # if the string is empty 
        if n == 0:
            return 1
        if n == 1:
            return 0 if s == "0" else 1
        res = 0
        last1, last2 = int(s[-1]), int(s[-2:])
        if last1 > 0:
            res += self.numDecodings(s[:-1])
        if 10 <= last2 <= 26:
            res += self.numDecodings(s[:-2])                
        return res


class Solution: # Time: O(n), space: O(n)
    @lru_cache(maxsize=None)
    def recursiveWithMemo(self, index, s):
        # If you reach the end of the string, return 1 for success
        # an empty string can only be decoded as an empty string
        if index == len(s):
            return 1
        # # If the string starts with a zero, it can't be decoded
        if s[index] == '0':
            return 0
        if index == len(s)-1:
            return 1
        answer = self.recursiveWithMemo(index+1, s)
        if int(s[index:index+2]) <= 26:
            answer += self.recursiveWithMemo(index+2, s)
        return answer
    
    def numDecodings(self, s: str) -> int:
        return self.recursiveWithMemo(0, s)

if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings("226"))  # 3



