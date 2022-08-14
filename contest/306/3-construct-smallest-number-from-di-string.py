"""
2375.
You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.

A 0-indexed string num of length n + 1 is created using the following conditions:

num consists of the digits '1' to '9', where each digit is used at most once.
If pattern[i] == 'I', then num[i] < num[i + 1].
If pattern[i] == 'D', then num[i] > num[i + 1].
Return the lexicographically smallest possible string num that meets the conditions.

Input: pattern = "IIIDIDDD"
Output: "123549876"
Explanation:
At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
Some possible values of num are "245639871", "135749862", and "123849765".
It can be proven that "123549876" is the smallest possible num that meets the conditions.
Note that "123414321" is not possible because the digit '1' is used more than once.
"""

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        l = len(pattern)
        res = []
        def backtrack(i, num, comb, visited):
            nonlocal res
            # early stop
            if len(comb) == l+1:
                res = comb[:]
                return True
            if num in visited:
                return
            # add num[i]
            comb.append(num)  
            visited.add(num)
            # next candidates for num[i+1]
            for n in range(1, 10):  
                # compare num[i] with num[i+1]
                if i+1 < l and pattern[i+1] == "I" and comb and comb[-1] >= n:
                    continue
                if i+1 < l and pattern[i+1] == "D" and comb and comb[-1] <= n:
                    continue
                if backtrack(i+1, n, comb, visited):
                    return True
            # backtracking
            comb.pop()
            visited.remove(num)
            
        for num in range(1, 10):
            # start from -1 to compare num[i] with num[i+1]
            if backtrack(-1, num, [], set()): # early stop
                break
        s = "".join([str(n) for n in res])
        return s
                    
            
            
