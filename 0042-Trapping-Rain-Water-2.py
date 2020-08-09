from typing import List
# find the highest left and right blocks
# get the minimum of these two blocks
# substract the oright height

class Solution:
    def trap(self, height: List[int]):
        forward, backward, fmax, bmax = [], [], 0, 0
        for h in height:
            fmax = max(fmax, h)
            forward.append(fmax)
        for h in reversed(height):
            bmax = max(bmax, h)
            backward.append(bmax)
        backward = reversed(backward)
        return sum(min(f,b)-h for f,b,h in zip(forward, backward, height))

    def trap(self, height: List[int]):
        ans, cur = 0, 0
        stack = []
        while cur < len(height):
            #print(cur, (stack[-1] if stack else ' '), height[cur], (height[stack[-1]] if stack else ' '), stack)
            while stack != [] and height[cur] > height[stack[-1]]:
                #print(cur, stack)
                top = stack.pop()
                #stack.pop() # mistake in C++ solutions
                if stack == []:
                    break
                distance = cur - stack[-1] - 1;
                bounded_height = min(height[cur], height[stack[-1]]) - height[top]
                ans += distance * bounded_height
            stack.append(cur)
            cur += 1
        return ans

        if not height:
            return 0


    def trap(self, height: List[int]):
        ans = 0
        stack = []
        for cur, cur_height in enumerate(height):
            #print(cur, cur_height, stack)
            while stack != [] and cur_height > height[stack[-1]]:
                top = stack.pop()
                if stack == []:
                    break
                distance = cur - stack[-1] - 1
                bounded_height = min(cur_height, height[stack[-1]]) - height[top]
                ans += distance * bounded_height
                #print('-->', stack, distance, bounded_height, ans)
            stack.append(cur)
        return ans

    def trap(self, height: List[int]):
        stack, res = [], 0
        for i, hi in enumerate(height):
            while stack and hi > height[stack[-1]]:
                bottom = stack.pop()
                res += 0 if not stack else (min(hi, height[stack[-1]])-height[bottom]) * (i-stack[-1]-1)
            stack.append(i)
        return res

"""
    def trap(self, height: List[int]):
        print([index for index, bar in enumerate(height) if bar > 0])
        start = next(index for index, bar in enumerate(height) if bar > 0) + 1
        end = len(height) - next(index for index, bar in enumerate(reversed(height)) if bar > 0) - 1
        left_max, right_max = max(height[:start]), max(height[end:])
        water = 0
        print(start, end)
        for index, bar in enumerate(height[start:end]):
            print(index, bar)
            water += min(left_max, right_max) - bar
            left_max = max(bar, left_max)
            if right_max == bar:
                right_max = max(height[index + 1:])
            print('-->', left_max, right_max)
        return water
"""

if __name__ == '__main__':
    s = Solution()
    
    #print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    #print(s.trap([0,3,2,2,4,1,5]))
    print(s.trap([4,3,2,1,2,3,4]))