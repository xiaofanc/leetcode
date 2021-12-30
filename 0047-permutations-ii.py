class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # consider each unique number as the candidate
        counter = collections.Counter(nums)
        results = []
        # build up the permutations base on the current combinations and the remaining numbers
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                results.append(comb[:]) # results.append(comb) does not work - need deep copy
                return
            for num in counter:
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -= 1
                    # print(comb)
                    # continue the exploration
                    backtrack(comb, counter)
                    
                    # revert the choice for the next exploration
                    comb.pop()
                    counter[num] += 1
        
        backtrack([], counter)
        return results

if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1,1,2])) # [[1,1,2],[1,2,1],[2,1,1]]