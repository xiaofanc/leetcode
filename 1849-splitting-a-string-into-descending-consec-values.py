"""
Check if we can split s into two or more non-empty substrings such that the numerical values of the substrings are in descending order and the difference between numerical values of every two adjacent substrings is equal to 1.

Input: s = "050043"
Output: true
Explanation: s can be split into ["05", "004", "3"] with numerical values [5,4,3].
The values are in descending order with adjacent values differing by 1.

Time: < O(2 ^ N)
https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/solutions/1186795/c-backtracking-solution-o-n-2-and-time-complexity-analytics/
Time could be O(N ^ 2). Even though we use backtracking here, it is obvious that the upper-bound complexity of this solution is N^2, in the for loop there is only one chance to go into the next function, so it is linear complexity O(N) for every iteration. 

Space: O(N)
"""

class Solution:
    def splitString(self, s: str) -> bool:
	
        def DFS(index, prev):
			# base case: no character left to split
            if index == n:
                return True
			# split the left substrings
            for j in range(index, n):
                val = int(s[index:j+1])
                if prev - val == 1 and DFS(j+1, val):
                    return True
		
		# split s to get prev
        n = len(s)
        for i in range(n-1):       # at least two substring
            val = int(s[:i+1])
            if DFS(i+1, val):
                return True
        return False 

    def splitString(self, s: str) -> bool:
        
        def backtrack(i, comb):
            if i == len(s) and len(comb) > 1:
                return True
            for j in range(i, len(s)):
                if not comb or comb[-1] - int(s[i:j+1]) == 1:
                    comb.append(int(s[i:j+1]))
                    if backtrack(j+1, comb):
                        return True
                    comb.pop()
            return False
        return backtrack(0, [])
        
if __name__ == '__main__':
    s = Solution()
    print(s.splitString("050043"))



    