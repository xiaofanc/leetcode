class Solution:
    def rotatedDigits(self, N: int) -> int:
        s1 = {"0","1","8", "2", "5", "6", "9"}
        s2 = {"2", "5", "6", "9"}
        count = 0
        for n in range(1, N+1):
            n = str(n)
            if all(c in s1 for c in n) and any(c in s2 for c in n):
                count += 1
        return count
            
                    
if __name__ == '__main__':
    s = Solution()
    print(s.rotatedDigits(100) == 40)             
    print(s.rotatedDigits(2) == 1)             
                
                
        