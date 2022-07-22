"""
There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.

calculate the accumulative sum for each row, get the most frequent sum..

"""
import collections

def leastBricks(wall):
    m = collections.defaultdict(int) # HashMap to help solve problem
    for row in wall:
        total = 0
        for brick in row[:-1]: # Exclude last index b/c the end is always a gap
            total += brick
            m[total] += 1
    if len(m) < 1: # Edge Case
        return len(wall)
    return len(wall) - max(m.values())

print(leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))