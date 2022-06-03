"""
check whether the overlap window >= duration:
how to get the overlap window?
  - max(start time), min(end time)
if not overlapping or overlap < duration:
  - check the next availability of the person who ends early
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
  print(s.meeting_planner([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 8))  # [60,68]
  print(s.meeting_planner([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 12))
