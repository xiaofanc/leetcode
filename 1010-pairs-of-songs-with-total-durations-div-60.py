from typing import List
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = [0] * 60
        ans = 0
        for i in range(len(time)):
            idx = time[i] % 60
            count[idx] += 1
        for i in range(1, 30):
            ans += count[i]*count[60-i]
        if count[0] >= 1:
            ans += count[0]*(count[0]-1)//2
        if count[30] >=1:
            ans += count[30]*(count[30]-1)//2
        return ans
    
        """
        count = 0
        for i in range(len(time)):
            for j in range(i+1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    count += 1
        return count
        """
        
                
if __name__ == '__main__':
    s = Solution()
    print(s.numPairsDivisibleBy60([30,20,150,100,40])) #3
    print(s.numPairsDivisibleBy60([60,60,60])) #3