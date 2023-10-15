class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        cars = set()
        for a, b in nums:
            for i in range(a, b+1):
                cars.add(i)
        return len(cars)

    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()
        res = 0
        prevs, preve = nums[0][0], nums[0][1]
        for s, e in nums[1:]:
            if prevs <= s <= preve:
                preve = max(preve, e)
            else:
                res += preve - prevs + 1
                prevs = s
                preve = e
        res += preve - prevs + 1
        return res