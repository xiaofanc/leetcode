"""
You are given an integer array ranks representing the ranks of some mechanics. ranksi is the rank of the ith mechanic. A mechanic with a rank r can repair n cars in r * n^2 minutes.

You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.

Return the minimum time taken to repair all the cars.

Note: All the mechanics can repair the cars simultaneously.

Method:
If a time value is feasible we will store it as answer and try to check lower time value for fisibility.

If a time value is not feasible then we mark it as lower limit and then keep
checking for higher time value for the fisibility.

To check if a time value is feasible or not, simply start repairing cars
for each rank with max possible value.
To do this for a rank r & time t, max car it can repir, n = sqrt(t / r);
"""
class Solution:
	# binary search the time
    def repairCars(self, A: List[int], cars: int) -> int:
        def repair(t):
            # total cars can be repaired with time t
            total = 0
            for i in range(len(A)):
                total += int(sqrt(t/A[i]))
            return total

        left, right = 1, min(A) * cars * cars

        while left < right:
            mid = (left + right) // 2
            if repair(mid) < cars:
                left = mid + 1
            else:
                right = mid
        return left
            
    def repairCars(self, A: List[int], cars: int) -> int:
        count = Counter(A)
        h = [[a, a, 1, count[a]] for a in count]

        heapify(h)
        while cars > 0:
            time, rank, k, count = heappop(h)
            # print("time, rank, k, count ", time, rank, k, count)
            # 剪掉time分钟内可以修好的车
            cars -= count
            # print("cars ", cars)
            k += 1
            heappush(h, [rank * k * k, rank, k, count])
        return time


        
