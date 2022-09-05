
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # 'a1b2'
        # 'A1b2', 'a1B2'
        # 'A1B2'
        arr = [char for char in s]
        res = []
        def backtrack(i, arr):
            res.append(''.join(arr[:]))
            for j in range(i, len(arr)):
                if arr[j].isalpha():
                    if arr[j].islower():
                        arr[j] = arr[j].upper()
                        backtrack(j+1, arr)
                        arr[j] = arr[j].lower()
                    else:
                        arr[j] = arr[j].lower()
                        backtrack(j+1, arr)
                        arr[j] = arr[j].upper()                        
        backtrack(0, arr)
        return res
                
