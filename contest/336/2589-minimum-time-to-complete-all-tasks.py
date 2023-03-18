# sort by end time
# For the task with the closest end time, the best strategy is to finish it as late as possible
# That way, we have the best chance for the computer time to be reused by tasks that end later. We use line to mark the computer "on" slots. When we process a task, we count "on" slots within the interval.
# If we still need additional time to finish the task, we pick available slots starting from the end time (as late as possible).



class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        usedTime = [False] * 2001
        # finish the task as late as possible
        tasks.sort(key=lambda x: x[1])
        for s, e, d in tasks:
            # reduce the time when the computer is already on
            for t in range(s, e + 1):
                d -= usedTime[t]
            # if more time is needed, start from end
            t = e
            while d > 0:
                if not usedTime[t]:
                    usedTime[t] = True
                    d -= 1
                t -= 1
        return sum(usedTime)

    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        usedTime = set()
        tasks.sort(key=lambda x: x[1])
        for s, e, d in tasks:
            for t in range(s, e + 1):
                if t in usedTime:
                    d -= 1
            t = e
            while d > 0:
                if t not in usedTime:
                    usedTime.add(t)
                    d -= 1
                t -= 1
        return len(usedTime)

        