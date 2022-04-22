"""
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Time: O(4^N * N)
It takes N steps to generate a single combination. Since there are in total 4^N possible combinations, at most it would take us 4^N * N steps to generate all combinations.

Space: O(N) where N is the length of digits
Not counting space used for the output, the extra space we use relative to input size is the space occupied by the recursion call stack. It will only go as deep as the number of digits in the input since whenever we reach that depth, we backtrack.
"""
from itertools import product

class Solution:
    # Time: O(n^2)
    def letterCombinations(self, digits: str) -> List[str]:
        smap = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        char = []
        for d in digits:
            char.append(smap[int(d)])
        # print(char)
        # print(product(*char))
        return ["".join(c) for c in product(*char) if c]
    
    # Time: O(4^N * N)
     def letterCombinations(self, digits: str) -> List[str]:
        smap = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        if not digits:
            return []
        
        def backtrack(index, path):
            if len(path) == len(digits):
                combinations.append("".join(path))
                return
            
            letters = smap[int(digits[index])]
            for letter in letters:
                path.append(letter)
                backtrack(index+1, path)
                path.pop() # backtrack
        
        combinations = []
        backtrack(0, [])
        return combinations

    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs","8":"tuv","9":"wxyz"}
        res = []
        n = len(digits)
        if n == 0:
            return res
        def backtrack(start, comb):
            if len(comb) == n:
                res.append(comb[:])
                return
            d = digits[start]
            for l in mapping[d]:
                comb += l
                backtrack(start+1, comb)
                comb = comb[:-1]
        backtrack(0,"")
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23")) # ["ad","ae","af","bd","be","bf","cd","ce","cf"]



    