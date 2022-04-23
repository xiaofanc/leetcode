"""
Check if we can split s into two or more non-empty substrings such that the numerical values of the substrings are in descending order and the difference between numerical values of every two adjacent substrings is equal to 1.

Input: s = "050043"
Output: true
Explanation: s can be split into ["05", "004", "3"] with numerical values [5,4,3].
The values are in descending order with adjacent values differing by 1.

Time: < O(N x N ^ N)
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

if __name__ == '__main__':
    s = Solution()
    print(s.splitString("050043"))



    