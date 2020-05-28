# O(n) using stack

from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:
            return 
        stack = []
        day_warmer = [0] * len(T)
        stack = [0]
        for i in range(1, len(T)):
            while stack and T[i] > T[stack[-1]]:
                prev = stack.pop()
                day_warmer[prev] = i-prev
            stack.append(i)
            #print(stack)
        return day_warmer
                
if __name__ == '__main__':
    s = Solution()
    print(s.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))

