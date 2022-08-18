
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        
        def backtrack(i, comb):
            if len(comb) >= 2:
                res.add(tuple(comb[:]))
                
            for j in range(i, len(nums)):
                if not comb or nums[j] >= comb[-1]:
                    comb.append(nums[j])
                    backtrack(j+1, comb)
                    comb.pop()
                else:
                    continue
        backtrack(0, [])
        return res

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i, comb):
            if len(comb) >= 2:
                res.append(tuple(comb[:]))
            
            # create a set for each level
            used = set()
            for j in range(i, len(nums)):
                if not comb or nums[j] >= comb[-1]:
                    # does not work when same elements are not consecutive
                    # if j > i and nums[j] == nums[j-1]:
                        # continue
                        
                    # skip j when same element has been used on the same level
                    # [1,2,1,1,1]
                    # when start = 0, j = 0 to 5, [1,2],[1,1],[1,1,1],[1,1,1,1]
                    # 1 will not be used since the first 1 was used
                    # remove duplicates when same elements are on the same level
                    # we will continue to add 1 like [1,1] since they are not are the same level
                    if nums[j] in used:
                        continue
                    used.add(nums[j])
                    comb.append(nums[j])
                    backtrack(j+1, comb)
                    comb.pop()
                else:
                    continue
        backtrack(0, [])
        return res
                                    
                
if __name__ == '__main__':
	s = Solution()
	print(s.findSubsequences([4,6,7,7])) # [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
	print(s.findSubsequences([4,4,3,2,1])) # [[4,4]]
	print(s.findSubsequences([1,1,1,1,1,1])) # [[1,1],[1,1,1],[1,1,1,1],[1,1,1,1,1],[1,1,1,1,1,1]]
	print(s.findSubsequences([1,2,1,1,1,1,1])) # [[1,2],[1,1],[1,1,1],[1,1,1,1],[1,1,1,1,1],[1,1,1,1,1,1]]


