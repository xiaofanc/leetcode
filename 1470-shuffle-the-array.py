class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1 = nums[:n]
        nums2 = nums[n:]
        for i in range(2*n):
            if i % 2 == 0:
                nums[i] = nums1[i//2]
            else:
                nums[i] = nums2[(i-1)//2]
        return nums

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i+n])
        return result
        
if __name__ == '__main__':
    s = Solution()
    print(s.shuffle([2,5,1,3,4,7], 3))
    print(s.shuffle([1,1,2,2], 2))
    print(s.shuffle([1,2,3,4,4,3,2,1], 4))