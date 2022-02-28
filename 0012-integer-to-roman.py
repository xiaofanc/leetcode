"""
The system we use to decide is to select the representation with the largest possible symbols, working from left to right.
"""

class Solution:
	# Greedy: time = space = O(1)
    def intToRoman(self, num: int) -> str:
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
          (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
          (5, "V"), (4, "IV"), (1, "I")]
        roman = []
        for value, symbol in digits:
            count, num = divmod(num, value)
            roman.append(symbol*count)
        return "".join(roman)

if __name__ == '__main__':
	s = Solution()
	print(s.intToRoman(1925)) # "MCMXXV"