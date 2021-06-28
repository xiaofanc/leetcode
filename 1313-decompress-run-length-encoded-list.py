class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        output = []
        for i in range(len(nums)//2):
            for j in range(nums[2*i]):
                output.append(nums[2*i+1])
        return output

    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        output = []
        for i in range(len(nums)//2):
            output.extend([nums[2*i+1]] * nums[2*i])
        return output

    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        return [nums[i+1] for i in range(0, len(nums), 2) for j in range(nums[i])]
        
if __name__ == '__main__':
    s = Solution()
    print(s.decompressRLElist([1,2,3,4]))
    print(s.decompressRLElist([1,1,2,3]))