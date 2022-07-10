"""
1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
5. If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -2^31 should be clamped to -2^31, and integers greater than 2^31 - 1 should be clamped to 2^31 - 1.
6. Return the integer as the final result.

"""

class Solution:
    def myAtoi(self, s: str) -> int:
        num = 0
        sign = 1
        index = 0 
        n = len(s)
        
        int_max, int_min = pow(2,31)-1, -pow(2,31)
        
        # removing leading 0
        while index < n and s[index] == " ":
            index += 1
        
        # decide positive or negative, could without "+/-"
        if index < n and s[index] == "-":
            sign = -1
            index += 1
        elif index < n and s[index] == "+":
            sign = 1
            index += 1
        
        while index < n and s[index].isdigit():
            digit = int(s[index])
            if num > int_max // 10 or (num == int_max // 10 and digit > int_max % 10): # > 7
                return int_max if sign == 1 else int_min
            num = num * 10 + digit
            index += 1
            
        return num * sign

if __name__ == '__main__':
  	s = Solution()
  	print(s.myAtoi("2147483648")) # 2147483647  
    print(s.myAtoi("-2147483647")) # -2147483647  
    print(s.myAtoi("-2147483648")) # -2147483648
  	print(s.myAtoi("-2147483649")) # -2147483648 - int_min
    print(s.myAtoi("   -0042uuun4")) # -42




