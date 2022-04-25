"""
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").

Methodology:
include arr[i] or not

Time: O(M x 2^N)
include arr[i] or not. M is the length of the concat string

Space: O(M)
"""

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        charset = set()
        def overlap(set1, set2):
            c = Counter(set1) + Counter(set2)
            return max(c.values()) > 1
        
        def backtrack(i):
            if i == n:
                return len(charset)
            
            res = 0
            # include arr[i]
            if not overlap(charset, arr[i]):
                for char in arr[i]:
                    charset.add(char)
                res = backtrack(i+1)
                for char in arr[i]:
                    charset.remove(char)
            # not include arr[i]
            return max(res, backtrack(i+1))
        
        return backtrack(0)
            
if __name__ == '__main__':
	s = Solution()
	print(s.maxLength(["un","iq","ues", "aple"])) # 8 ["un","iq","aple"]           

                
        
            
            
            
