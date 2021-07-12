class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        count = int(math.sqrt(c))
        dct = set()
        for i in range(count+1): 
            a2 = i**2
            dct.add(a2)  # add first - 0
            if c - a2 in dct:
                return True
        return False
    
            
     def judgeSquareSum(self, c: int) -> bool:
        a = 0
        count = int(math.sqrt(c))
        
        for a in range(count+1): 
            b = c - a*a
            i = 1
            s = 0
            # check if b is a perfect square
            # a perfect square can be represented as a sum of first n odd positive integers
            # check if b can be represented as a sum of ...
            while s < b:
                s += i
                i += 2
            if s == b:
                return True
        return False
                   
if __name__ == '__main__':
    s = Solution()
    print(s.judgeSquareSum(5))  #True
    print(s.judgeSquareSum(0))  #True

                
            
        