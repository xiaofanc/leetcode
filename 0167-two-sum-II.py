from typing import List
class Solution: #numbers is sorted
    def twoSum0(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i
            
                
    # two-pointer
    def twoSum1(self, numbers, target):
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1

    # dictionary           
    def twoSum2(self, numbers, target):
        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i

    # binary search        
    def twoSum3(self, numbers, target):
        for i in range(len(numbers)):
            l, r = i+1, len(numbers)-1
            #print(i, l, r)
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1

s=Solution()
print(s.twoSum0([1,2,2,7,11,15],9))
print(s.twoSum1([1,2,2,7,11,15],9))
print(s.twoSum2([1,2,2,7,11,15],9))
print(s.twoSum3([1,2,2,7,11,15],9))