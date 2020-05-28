from typing import List

class Solution:
    #solution2 DP;
    #find the max from left and right 
    def trap(self, height: List[int]) -> int:
        forward, fmax = [], 0
        for h in height:
            fmax = max(fmax,h)
            forward.append(fmax)

        backward, bmax = [], 0
        for h in reversed(height):
            bmax = max(bmax,h)
            backward.append(bmax)
        backward = backward[::-1]
        
        return sum(min(b,f)-h for b,f,h in zip(forward,backward,height))
    
    def trap(self, height: List[int]) -> int:
        ans, cur = 0, 0
        stack = []
        for cur, cur_height in enumerate(height):
            while stack != [] and cur_height > height[stack[-1]]:
                top = stack.pop()
                if stack == []:
                    break
                distance = cur - stack[-1] - 1
                #find minimum of left and right, 
                bounded_height = min(cur_height, height[stack[-1]]) - height[top]
                ans += distance * bounded_height
            stack.append(cur)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))