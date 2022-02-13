"""
minute pointer: 6'/minute
hour pointer: 30'/hour
case when minute = 0: res = 30 * hour
case when minute > 0: hour angle: (hour % 12 + minutes / 60) * 30'

The angle between minute hand and 0-minutes vertical line is minutes_angle = 6 * minutes
The angle between hour hand and 12-hour vertical line is hour_angle = (hour % 12 + minutes / 60) * 30
Find the difference: diff = abs(hour_angle - minutes_angle)
Return the smallest angle: min(diff, 360 - diff)

"""

class Solution:
	# Time: O(1)
    def angleClock(self, hour: int, minutes: int) -> float:
        
        angle_per_hour = 30
        angle_per_min = 6
        
        # The angle between hour hand and 12-hour vertical line
        hour_angle = (hour % 12 + minutes / 60) * angle_per_hour
        # The angle between minute hand and 0-minutes vertical line 
        min_angle = minutes * angle_per_min
        diff = abs(hour_angle - min_angle)
        return min(diff, 360-diff)
 
if __name__ == '__main__':
	s = Solution()
	print(s.angleClock(12, 30)) # 165



