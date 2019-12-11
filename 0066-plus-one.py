class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = [str(i) for i in digits]
        intdigits = int("".join(s))
        plusone = intdigits + 1
        return str(plusone)


    def plusOne(digits):
    num = 0
    for i in range(len(digits)):
    	num += digits[i] * pow(10, (len(digits)-1-i))
    return [int(i) for i in str(num+1)]
    

if __name__ == '__main__':
	s = Solution()
	print(s.plusOne([9,9,9,9]))