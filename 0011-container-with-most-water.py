# Find two lines, which together with x-axis forms a container, such that the
# container contains the most water.

# Note: You may not slant the container and n is at least 2.
# 长度越宽越好 所以从两边开始，面积受到短边的限制 所以移动较短的那边

class Solution:
    # The area formed between the lines will always be limited by the height of the shorter line
    # Further, the farther the lines, the more will be the area obtained.
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxarea = 0
        while left < right:
            maxarea = max(maxarea, (right-left)*min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return maxarea
                
            
        
