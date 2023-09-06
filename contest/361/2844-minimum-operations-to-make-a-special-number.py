"""
You are given a 0-indexed string num representing a non-negative integer.

In one operation, you can pick any digit of num and delete it. Note that if you delete all the digits of num, num becomes 0.

Return the minimum number of operations required to make num special.

An integer x is considered special if it is divisible by 25.

Input: num = "2245047"
Output: 2
Explanation: Delete digits num[5] and num[6]. The resulting number is "22450" which is special since it is divisible by 25.
It can be shown that 2 is the minimum number of operations required to get a special number.

"""
class Solution:
    def minimumOperations(self, num: str) -> int:
        # A number is divisible by 25 if it ends with 00, 25, 50, or 75 / 0
        zero, two, five, seven = 0, 0, 0, 0
        n = len(num)
        for i in range(len(num)-1,-1,-1):
            if num[i] == "0":
                zero += 1
                if zero == 2:
                    return n-i-2
            elif num[i] == "2":
                two += 1  
                if two >= 1 and five >= 1: # 255, 25522222
                    return n-i-2
            elif num[i] == "5":
                five += 1
                if five >= 1 and zero >= 1:
                    return n-i-2
            elif num[i] == "7":
                seven += 1
                if seven >= 1 and five >= 1:
                    return n-i-2
        if zero == 1:
            return n-1
        return n
            
         
class Solution:
    def minimumOperations(self, num: str) -> int:
        zero, five = False, False
        l = len(num)
        for i in range(len(num)-1,-1,-1):
            n = num[i]
            if zero and n == "0": return l-i-2
            if zero and n == "5": return l-i-2
            if five and n == "2": return l-i-2
            if five and n == "7": return l-i-2
            if n == "0":
                zero = True
            if n == "5":
                five = True
        if zero:
            return l-1
        return l


           
