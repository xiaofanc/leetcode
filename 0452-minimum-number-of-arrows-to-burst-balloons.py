class Solution:
    
    # time: O(nlogn), space: O(n) 
    # - list.sort() function in Python is implemented with the Timsort algorithm whose space complexity is O(n).
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # sort the balloon by the end 
        points.sort(key = lambda x: x[1])
        
        # check if the start of next ballon is < the first_end
        # if yes, do nothing
        # if no, add one arrow and update the first_end
        first_end = points[0][1]
        arrow = 1
        for start, end in points[1:]:
            # print(first_end, start)
            if first_end >= start:
                continue
            else:
                arrow += 1
                first_end = end
                # print(first_end)
                # print('arrow', arrow)
        return arrow

if __name__ == '__main__':
    s = Solution()
    print(s.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]])) # 2
    print(s.findMinArrowShots([[[3,4], [1,6], [5,8], [7,12], [10,16]]])) # 3
