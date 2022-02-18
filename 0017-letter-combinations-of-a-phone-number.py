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

if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23")) # ["ad","ae","af","bd","be","bf","cd","ce","cf"]



    