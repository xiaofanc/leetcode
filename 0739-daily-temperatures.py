# O(n) using stack, pop out the prev idx if meeting a warmer temp and calculate the diff

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures) 
        for i, temperature in enumerate(temperatures):
            #print('temperature',temperature)
            while stack and temperature > stack[-1][1]:
                prev, t = stack.pop()
                res[prev] = i-prev
            stack.append([i, temperature])
            #print('stack', stack)
            #print('res', res)
        return res


    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # only store index
        res = [0] * len(temperatures)
        for cur, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                res[prev_day] = cur - prev_day
            stack.append(cur)
        return res
        
if __name__ == '__main__':
    s = Solution()
    print(s.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))

