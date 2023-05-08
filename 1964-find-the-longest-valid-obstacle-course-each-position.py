


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        res = []
        LIS = [] # the lowest last obstacle's height of the sequence with length i+1
        for i, obs in enumerate(obstacles):
            # find the longest course end by the current obstacle with h
            # find the first number > obs
            idx = bisect.bisect_right(LIS, obs) 
            if idx == len(LIS):
                LIS.append(obs)
            else:
                LIS[idx] = obs
            res.append(idx+1)
        return res