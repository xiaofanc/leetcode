"""
Implement a function meetingPlanner that given the availability, slotsA and slotsB, of two people and a meeting duration dur, returns the earliest time slot that works for both of them and is of duration dur. If there is no common time slot that satisfies the duration requirement, return an empty array.


input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 8
output: [60, 68]

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 12
output: []

"""

def meeting_planner(slotsA, slotsB, dur):
  a, b = 0, 0
  while a < len(slotsA) and b < len(slotsB):
    start = max(slotsA[a][0], slotsB[b][0])
    end = min(slotsA[a][1], slotsB[b][1])
    
    if start + dur <= end:
      return [start, start+dur]
    if slotsA[a][1] < slotsB[b][1]:
      a += 1
    else:
      b += 1
  return []

if __name__ == '__main__':
	s = Solution()
	print(s.meeting_planner([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 8))
	print(s.meeting_planner([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 12)


