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

    def maxLength(self, arr: List[str]) -> int:
        
        def check(set1, lst):
            set2 = set(lst)
            if len(set2) != len(lst):
                return False
            for char in set1:
                if char in set2:
                    return False
            return True
        
        charSet = set()
        maxL = 0
        def backtrack(i):
            nonlocal maxL
            if len(charSet) > maxL:
                maxL = len(charSet)
            if i == len(arr):
                return
            if check(charSet, arr[i]):
                for char in arr[i]:
                    charSet.add(char)
                backtrack(i+1)
                for char in arr[i]:
                    charSet.remove(char)
            
            backtrack(i+1)
        backtrack(0)
        return maxL
        
    def maxLength(self, arr: List[str]) -> int:
        
        def check(comb):
            seen = set()
            for char in comb:
                if char in seen:
                    return False
                seen.add(char)
            return True
        
        maxL = 0
        def backtrack(i, comb):
            nonlocal maxL
            # print("comb->", comb)
            string = "".join(comb)
            if check(string) and len(string) > maxL:
                maxL = len(string)
            for j in range(i, len(arr)):
                comb.append(arr[j])
                backtrack(j+1, comb)
                comb.pop()
        
        backtrack(0, [])
        return maxL

    def maxLength(self, arr: List[str]) -> int:
        res = 0

        def subsets(start, comb):
            nonlocal res
            res = max(res, len(comb))
            if start == len(arr):
                return
            for i in range(start, len(arr)):
                # check if arr[i] has duplicates and arr[i] has the duplicate char compared to comb
                unique = (len(set(comb+arr[i])) == len(comb+arr[i]))
                if not unique:
                    continue
                subsets(i+1, comb+arr[i])
        subsets(0, "")
        return res

if __name__ == '__main__':
	s = Solution()
	print(s.maxLength(["un","iq","ues", "aple"])) # 8 ["un","iq","aple"]           
    print(s.maxLength(["aa","bb"])) # 0

                
        
            
            
            
