'''
jumping number: 123, 654, 34565456
write a function to return all jumping numbers between 1 and n.
n = 25
1,2,3,4,5,6,7,8,9
10, 12, 21, 23

# loop over 1 to n and check if the number is a jumping number
# how to check a jumping number?
    transform it into a string
    if len(str) == 1: append the integer
    else: compare the digit with the next digit for the integer
'''

def findJumpingNum1(n):
    res = []
    def isJumpingNum(i):
        s = str(i)
        if len(s) == 1:
            return True
        else:
            # check the digits in the string
            for j in range(len(s)-1):
                if abs(int(s[j])-int(s[j+1])) != 1:
                    return False
            return True
                
    for i in range(1, n+1):  
        if isJumpingNum(i): 
            res.append(i)
    return res
        
def findJumpingNum2(n):
    res = []
    digits = len(str(n))
    for i in range(1, digits+1): # digits in the jumping number
        if i == 1:
            # find the jumping numbers which have 1 digits and <= n
            for j in range(10): # the number in that digit
                if i == 1 and j == 0: # [1,2,3,4,...9] 
                    continue
                elif j <= n:
                    res.append(j)
                else:
                    return res
        # use the digits in the res
        for m in res:
            if len(str(m)) == i-1:
                if m%10 >= 1:
                    num1 = m*10 + (m%10-1)
                    if num1 <= n: 
                        res.append(num1)
                    else:
                        return res
                if m%10 < 9: 
                    num2 = m*10 + (m%10+1)
                    if num2 <= n:
                        res.append(num2)
                    else:
                        return res
            
            
print("finding jumping numbers", findJumpingNum1(400)) 
print("finding jumping numbers", findJumpingNum2(400)) 

