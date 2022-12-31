class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sortedTask = []
        for i, task in enumerate(tasks):
            sortedTask.append((task[0], task[1], i))
        sortedTask.sort()

        # minheap for available tasks (processTime, index)
        available = []
        res = []
        curTime = 0
        i = 0
        while available or i < len(sortedTask):
            if not available and curTime < sortedTask[i][0]:
                # update cur time using enqueue time 
                curTime = sortedTask[i][0]
            # add available tasks
            while i < len(sortedTask) and curTime >= sortedTask[i][0]:
                heapq.heappush(available, (sortedTask[i][1], sortedTask[i][2]))
                i += 1
            pt, idx = heapq.heappop(available)
            curTime += pt
            res.append(idx)
        return res


