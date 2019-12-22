from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses = sorted(houses)
        heaters = sorted(heaters)
        heaters = [float("-inf")] + heaters + [float("inf")]
        i, ans = 0, 0
        for house in houses:
            while house > heaters[i+1]:
                i += 1
            dis = min(house - heaters[i], heaters[i+1] - house)
            ans = max(ans, dis)
        return ans

    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses = sorted(houses)
        heaters = sorted(heaters)
        heaters = heaters + [float("inf")]
        i, ans = 0, 0
        for house in houses:
            # house is more close to heaters[i+1]
            while house >= sum(heaters[i:i+2])/2:
                i += 1
            # if house if more close to heaters[i], then house > heaters[i]
            ans = max(ans, abs(heaters[i] - house))
        return ans
            
if __name__ == '__main__':
    s = Solution()
    print(s.findRadius([282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923],[823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]))
            
            