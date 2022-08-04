"""
solution 1: divide and conquer
This approach relies on the observation that the rectangle with maximum area will be the maximum of:
The widest possible rectangle with height equal to the height of the shortest bar.
The largest rectangle confined to the left of the shortest bar(subproblem).
The largest rectangle confined to the right of the shortest bar(subproblem).

solution 2: using stack
In this approach, we maintain a stack. Initially, we push a -1 onto the stack to mark the end. We start with the leftmost bar and keep pushing the current bar's index onto the stack until we get two successive numbers in descending order, i.e. until we get heights[i] < heights[i-1]. Now, we start popping the numbers from the stack until we hit a number stack[j] on the stack such that heights[stack[j]] <= heights[i].

[1,2,3,4,2]
stack = [-1,0,1,2,3] -> store index
when i = 4, 
    heights[4] = 2 < heights[3] = 4, pop out index 3
    calculate the maxarea using heights[3] = 4 as height and 
    width = i-stack[-1]-1 = 4-2-1 = 1
    maxarea for using heights[3] = 4 as height is 4*1 = 4

    heights[4] = 2 < heights[2] = 3, pop out index 2
    calculate the max area of rectangle using 3 as height
    the width = 4-1-1 = 2 
    Intuition is how much that height can extend from left to right
Finally,
stack = [-1,0,4], which means that height in index 0 and index 4 can extend to the end!
    pop out the index to get height = heights[i]
    width = len(heights)-stack[-1]-1
    for index = 0, width = 5-(-1)-1 = 5
"""
class Solution:
	# average time: O(nlogn), worse time: O(n^2), space: O(n)	
    def largestRectangleArea(self, heights: List[int]) -> int:
        def calculatearea(heights, start, end):
            if start > end:
                return 0
            minindex = start
            for i in range(start, end+1):
                if heights[i] < heights[minindex]:
                    minindex = i
            return max(heights[minindex] * (end - start + 1), calculatearea(heights, start, minindex-1), calculatearea(heights, minindex+1, end))
        
        return calculatearea(heights, 0, len(heights)-1)
    
    # Time: O(n)               
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
                current_height = heights[stack.pop()]
                current_width = i - stack[-1] - 1
                max_area = max(max_area, current_height * current_width)
            stack.append(i)
        
        # deal with the last height
        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            current_width = len(heights) - stack[-1] - 1
            max_area = max(max_area, current_height * current_width)
        return max_area

if __name__ == '__main__':
	s = Solution()
	print(s.largestRectangleArea([2,1,5,6,2,3])) #10



	