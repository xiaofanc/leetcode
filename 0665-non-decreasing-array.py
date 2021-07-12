class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        def mono_increasing(arr):
            for i in range(len(arr)-1):
                if arr[i] > arr[i+1]:
                    return False 
            return True
        
        new = nums[:]
        for i in range(len(nums)):
            old_i = nums[i]
            new[i] = new[i-1] if i > 0 else float('-inf')
            if mono_increasing(new):
                return True
            new[i] = old_i
        return False
            

    def checkPossibility(self, nums: List[int]) -> bool:
        # when it has >= 2 violations (first > second)
        violations = 0
        for i in range(len(nums)-1):            
            if nums[i+1] < nums[i]: 
                # 4 2 1 -> 2 2 1
                if i == 0:
                    nums[i] = nums[i+1]
                # if i is in the middle, compare nums[i-1] with nums[i+1]
                # 3 4 5(i) 3 6 8 -> 3 4 5 5 6 8
                elif i > 0 and nums[i-1] > nums[i+1]:
                    nums[i+1] = nums[i]
                # 1 2 5(i) 3 6 8 -> 1 2 3 3 6 8
                else: 
                    nums[i] = nums[i+1]
                # print(nums)
                violations += 1
        if violations >= 2:
            return False
        return True

    def checkPossibility(self, nums: List[int]) -> bool:
        violations = 0
        for i in range(1, len(nums)):    
            if nums[i-1] > nums[i]:
                if violations == 1:
                    return False
                violations += 1
                
                # 1 2 5 3(i) 6 8 -> 1 2 3 3 6 8
                # 4 2 1 -> 2 2 1
                if i < 2 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                # 3 4 5 3(i) 6 8 -> 3 4 5 5 6 8
                else:
                    nums[i] = nums[i-1]
                    
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.checkPossibility([4,2,3])) # True [1,2,3]
    print(s.checkPossibility([4,2,1])) # False





