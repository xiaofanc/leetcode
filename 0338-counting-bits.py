class Solution:
    def countBits(self, num: int) -> List[int]:
        return [bin(i).count("1") for i in range(num+1)]
        

if __name__ == '__main__':
    s = Solution()
    print(s.countBits(5) == [0,1,1,2,1,2])