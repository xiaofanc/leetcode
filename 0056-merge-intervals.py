# Given a collection of intervals, merge all overlapping intervals.

class Solution:
    # Time: O(nlogn), space: O(n)
    # runtime is dominated by the O(nlogn) complexity of sorting
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort()
        for interval in intervals:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(interval[1], merged[-1][1])
        return merged
                
if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1,3],[2,6],[4,10],[15,18]]) == [[1,10],[15,18]])