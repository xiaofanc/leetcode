from typing import List

class Solution:
    #solution2 DP;
    #find the max from left and right 
    def trap(self, height: List[int]) -> int:
        forward, fmax = [], 0
        for h in height:
            fmax = max(fmax,h) # why? min(b,f)-h could be neg if no max
            forward.append(fmax)

        backward, bmax = [], 0
        for h in reversed(height):
            bmax = max(bmax,h)
            backward.append(bmax)
        backward = backward[::-1]
        
        return sum(min(b,f)-h for b,f,h in zip(forward,backward,height))
    
    # monotonic stack
    def trap(self, height: List[int]) -> int:
        ans, cur = 0, 0
        stack = [] # store index
        for cur, cur_height in enumerate(height):
            while stack != [] and cur_height > height[stack[-1]]:
                top = stack.pop()
                if stack == []:
                    break
                # calculate width between left and right block
                # left and right are all higher than top since it is a monotonic stack
                distance = cur - stack[-1] - 1
                # height difference between min(left, right) and top
                bounded_height = min(cur_height, height[stack[-1]]) - height[top]
                ans += distance * bounded_height
            stack.append(cur)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(s.trap([4,2,0,3,2,5]))  # 9 = 2+2+1+4
