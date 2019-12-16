class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        def isleap(year):
            if year % 4 != 0:
                return False
            elif year % 100 != 0:
                return True
            elif year % 400 != 0:
                return False
            else:
                return True
        daysinmonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        daysinweek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        # 1971,1,1 - Friday
        diff = 5
        for y in range(1971, year):
            if isleap(y): 
                diff += 366
            else: 
                diff += 365
        for m in range(0, month-1):
            diff += daysinmonth[m]
        if month >= 2 and isleap(year):
            diff += 1
        diff += day - 1
        print(diff)
        return daysinweek[diff % 7]

if __name__ == '__main__':
    s = Solution()
    print(s.dayOfTheWeek())