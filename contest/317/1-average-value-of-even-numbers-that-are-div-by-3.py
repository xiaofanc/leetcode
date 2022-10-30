
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        numbers = []
        for n in nums:
            if n % 6 == 0:
                numbers.append(n)
        return sum(numbers) // len(numbers) if numbers else 0