"""
3//2 = 1
-3//2 = -2
int(3/2) = 1
int(-3/2) = -1

no need to add +0 if add condition (or i == len(s)-1)
"""


class Solution:

    # time: O(n), space: O(n)
    def calculate(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        
        s += "+0"  # to calculate the last expression 3/2
        #print(s)
        currentNumber = 0
        operation = "+"  # sign for first number
        stack = []   # store pos/neg value, pop when previous operation is * or /
        for i in range(len(s)):
            if s[i].isdigit():
                currentNumber = currentNumber*10 + int(s[i])
            elif not s[i].isspace():    # or i == len(s)-1           
                if operation == "-":
                    #print('-', stack, currentNumber)
                    stack.append(-currentNumber)
                elif operation == "+":
                    #print('+', stack, currentNumber)
                    stack.append(currentNumber)
                elif operation == "*":
                    #print('*', stack, currentNumber)
                    stack.append(stack.pop() * currentNumber)
                else:
                    #print('/', stack, currentNumber)
                    stack.append(int(stack.pop() / currentNumber))
                
                operation = s[i] # store the sign of the number before the current sign
                currentNumber = 0
                
        return sum(stack)

if __name__ == '__main__':
    s = Solution()
    print(s.calculate(14-3/2))  # 13
    print(s.calculate(3+2*2))  # 7




