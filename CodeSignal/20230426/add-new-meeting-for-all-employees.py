"""
schedules represent for meetings j for employee i
add a new meeting of length l for all employees when they can all attend
return the earliest start time for the mew meeting
the new meeting must end before 24x60

schedules = [[[60,150],[180,240]], [[0,210],[360,420]]]
length = 120
res = 240

schedules = [[[480,510]], [[240,330]], [[375,400]]]
length = 180
res = 0

schedules = [[],[],[]]
length = 75
res = 0

schedules = [[0,1439],[[0,390],[480,510]],[]]
length = 90
res = -1
"""
import heapq
def add_new_meeting_for_all(schedules, length):
	res = 0
	h = []
	for i in range(len(schedules)):
		if len(schedules[i]) == 0: # no meetings
			continue
		else:
			heapq.heappush(h, (schedules[i][0], 0, i))

	while h:
		t, j, i = heapq.heappop(h)
		if res + length <= t[0]: # next start time
			return res
		res = max(res, t[1])     # next end time
		# push the next meeting
		if j+1 < len(schedules[i]):
			heapq.heappush(h, (schedules[i][j+1], j+1, i))
	if res + length <= 1440: # end of last meeting
		return res
	return -1



schedules = [[[60,150],[180,240]], [[0,210],[360,420]]]
length = 120
print(add_new_meeting_for_all(schedules, length))
# res = 240

schedules = [[[480,510]], [[240,330]], [[375,400]]]
length = 180
print(add_new_meeting_for_all(schedules, length))
# res = 0

schedules = [[],[],[]]
length = 75
print(add_new_meeting_for_all(schedules, length))
# res = 0

schedules = [[[0,1439]],[[0,390],[480,510]],[]]
length = 90
print(add_new_meeting_for_all(schedules, length))
# res = -1


