"""
Given an array of schedule that represents the schedule of bus arrival times and a string time that represents the current time.
Find out how many minutes ago the last bus left. If the first bus has yet to leave, return -1.
If the bus is scheduled to leave at the current time, it has not left yet.

schedule = ["12:30", "14:00", "19:55"], time = "14:30"
res = 30

schedule = ["00:00", "14:00", "19:55"], time = "00:00"
res = -1

schedule = ["12:30", "14:00", "19:55"], time = "14:00"
res = 90
"""

def bus_schedule(schedules, time):
	h0, m0 = time.split(":")
	h0, m0 = int(h0), int(m0)
	for i, sche in enumerate(schedules):
		h1, m1 = sche.split(":")
		h1, m1 = int(h1), int(m1)
		# find the first time >= h0:m0
		if h0 < h1 or (h0 == h1 and m1 >= m0):
			if i == 0:
				return -1
			else:
				hl, ml = schedules[i-1].split(":")
				hl, ml = int(hl), int(ml)
				return (h0-hl) * 60 + (m0-ml)
	# all time < h0:m0
	hl, ml = schedules[-1].split(":")
	hl, ml = int(hl), int(ml)
	return (h0-hl) * 60 + (m0-ml)


schedules = ["12:30", "14:00", "19:55"]
time = "14:30"
# res = 30
print(bus_schedule(schedules, time))

schedules = ["00:00", "14:00", "19:55"]
time = "00:00"
# res = -1
print(bus_schedule(schedules, time))

schedules = ["12:30", "14:00", "19:55"]
time = "14:00"
# res = 90
print(bus_schedule(schedules, time))

