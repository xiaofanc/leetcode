class Solution:

	#What about the range of numbers in between 2 multiples of 9?
	#Number:        18, 19, 20, 21, 22, 23, 24, 25, 26, 27
	#Sum of Digits: 9,  1,  2,  3,  4,  5,  6,  7,  8,  9
	#Number % 9:    0,  1,  2,  3,  4,  5,  6,  7,  8,  0

    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9 

    def addDigits(self, num: int) -> int:
        while num >= 10:
            temp = 0
            while num > 0:
                temp += num % 10
                num = num // 10
            num = temp
        return num

    def addDigits(self, num: int) -> int:
        #while num >= 10:
        #    num = sum(list(map(int, str(num))))
        #return num
    
        while num>9:
            num=sum(int(c) for c in str(num))
        return num

if __name__ == '__main__':
	s = Solution()
	print(s.addDigits(38))