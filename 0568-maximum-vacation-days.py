"""
https://leetcode.com/problems/maximum-vacation-days/discuss/102680/Python-Simple-with-Explanation

"""
class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        n, k = len(days), len(days[0]) # n cities, k weeks
        max_vacation = [0] + [float('-inf') for _ in range(n-1)]

        for week in range(k):
            curr = [float('-inf') for _ in range(n)]

            for dep_city in range(n):
                for arr_city, flight_exists in enumerate(flights[dep_city]):
                    if flight_exists or dep_city == arr_city:
                        curr[arr_city] = max(curr[arr_city], max_vacation[dep_city] + days[arr_city][week])

            max_vacation = curr

        return max(max_vacation)