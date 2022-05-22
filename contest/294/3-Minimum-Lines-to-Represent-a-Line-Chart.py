"""
You are given a 2D integer array stockPrices where stockPrices[i] = [dayi, pricei] indicates the price of the stock on day dayi is pricei. A line chart is created from the array by plotting the points on an XY plane with the X-axis representing the day and the Y-axis representing the price and connecting adjacent points.
Return the minimum number of lines needed to represent the line chart.
"""

class Solution:
	# 72 / 79 test cases passed -precision??
    def minimumLines(self, s: List[List[int]]) -> int:
        res = 1
        if len(s) == 1:
            return 0
        if len(s) == 2:
            return 1
        for i in range(1, len(s)-1):
            k1 = (s[i][1] - s[i-1][1]) / (s[i][0] - s[i-1][0])
            k2 = (s[i+1][1] - s[i][1]) / (s[i+1][0] - s[i][0])
            if k1 != k2:
                res += 1
        return res

if __name__ == '__main__':
	s = Solution()
	print(s.minimumLines([[72,98],[62,27],[32,7],[71,4],[25,19],[91,30],[52,73],[10,9],[99,71],[47,22],[19,30],[80,63],[18,15],[48,17],[77,16],[46,27],[66,87],[55,84],[65,38],[30,9],[50,42],[100,60],[75,73],[98,53],[22,80],[41,61],[37,47],[95,8],[51,81],[78,79],[57,95]])) # 29?