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
            
            
if __name__ == '__main__':
    s = Solution()
    print(s.checkPossibility([4,2,3]))