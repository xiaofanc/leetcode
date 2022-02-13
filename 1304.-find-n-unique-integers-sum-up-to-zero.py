"""
n = 0: [0]
n = 1: [0]
n = 2: [-1,1]
n = 3: [-1,1,0]
n = 4: [-2,-1,1,2]
n = 5: [-2,-1,1,2,0]


option 2: range(1-n, n, 2)
n = 1, [0]
n = 2, [-1, 1]
n = 3, [-2, 0, 2]
n = 4, [-3, -1, 1, 3]
n = 5, [-4, -2, 0, 2, 4] 

"""
class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        if n == 0 or n == 1:
            return [0]
        for i in range(1, n//2+1):
            res.extend([i, -i])
        if n % 2 == 1:
            res.append(0)
        return res
        
        # return range(1-n, n, 2)

if __name__ == '__main__':
    s = Solution()
    print(s.sumZero(5))  # [1,-1,2,-2,0]