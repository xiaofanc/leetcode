    class Solution:
        def findOriginalArray(self, changed: List[int]) -> List[int]:
            nums = collections.Counter(changed) # cannot use set here: [1,2,2,2,4,4]
            changed.sort()  # get the smaller int first, then find its double
            res = []
            for i, n in enumerate(changed):
                # if not deleted, then try to find its double
                if changed[i] in nums: 
                    res.append(changed[i])
                    nums[changed[i]] -= 1
                    if nums[changed[i]] == 0:
                        del nums[changed[i]]
                    double = changed[i]*2
                    if double in nums:
                        nums[double] -= 1
                        if nums[double] == 0:
                            del nums[double]
                    else:
                        return []
            return res


if __name__ == '__main__':
    s = Solution()
    print(s.findOriginalArray([2,1,2,4,2,4])) # [2,1,2]
    print(s.findOriginalArray([0,0,0,0])) # [0,0]
    print(s.findOriginalArray([0])) # []
    print(s.findOriginalArray([1])) # []
