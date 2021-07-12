# O(n) using stack

from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:
            return 
        day_warmer = [0] * len(T)
        stack = [0]
        for i in range(1, len(T)):
            while stack and T[i] > T[stack[-1]]:
                prev = stack.pop()
                day_warmer[prev] = i-prev
            stack.append(i)
            #print(stack)
        return day_warmer

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


if __name__ == '__main__':
    s = Solution()
    print(s.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))

