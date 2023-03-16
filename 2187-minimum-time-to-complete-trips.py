class Solution:
    # Time: O(nlogmk)
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 1, totalTrips * min(time) # max time needed to finish all trips
        # find the min t where sum of trips >= totalTrips
        while left <= right:
            mid = left + (right - left) // 2
            s = sum([mid // t for t in time])
            if s < totalTrips:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
