"""
2384.
You are given a string num consisting of digits only.

Return the largest palindromic integer (in the form of a string) that can be formed using digits taken from num. It should not contain leading zeroes.

Input: num = "444947137"
Output: "7449447"
Explanation: 
Use the digits "4449477" from "444947137" to form the palindromic integer "7449447".
It can be shown that "7449447" is the largest palindromic integer that can be formed.

Input: num = "00009"
Output: "9"
Explanation: 
It can be shown that "9" is the largest palindromic integer that can be formed.
Note that the integer returned should not contain leading zeroes.
"""

class Solution:
    def largestPalindromic(self, num: str) -> str:
        ans = ''
        c = collections.Counter(num)
        single = ''
        for d in '9876543210':
            cnt = c[d]
            if c[d] % 2:
                single = max(single, d)
            ans += d * (c[d] // 2)    
            # print("ans->", ans)
        idx = 0            
        for i, v in enumerate(ans):            
            idx = i
            if v != '0':
                break
        # else:                
            # idx = len(ans) + 1
        if ans.count('0') == len(ans):
            idx = len(ans) + 1
        # print("ix->", idx)
        ans = ans[idx:]    
        ans = ans + single + ans[::-1] 
        return ans if ans else '0'  




